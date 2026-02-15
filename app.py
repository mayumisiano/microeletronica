"""
🔬 Microeletrônica no Brasil — Dashboard Interativo

Dashboard Streamlit para análise de séries temporais do setor
de microeletrônica no Brasil (2006–2019).

Executar com:
    streamlit run app.py
"""

import streamlit as st

from src.data_loader import carregar_todos, verificar_dados, Dataset
from src import charts

# ---------------------------------------------------------------------------
# Configuração da página
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Microeletrônica no Brasil",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# CSS customizado
# ---------------------------------------------------------------------------

st.markdown("""
<style>
    /* Cabeçalho principal */
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6c757d;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    /* Cards de métricas */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 16px 20px;
        color: white;
    }
    div[data-testid="stMetric"] label {
        color: rgba(255,255,255,0.85) !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: white !important;
        font-size: 1.8rem !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        color: rgba(255,255,255,0.9) !important;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    /* Dividers */
    hr {
        border: none;
        border-top: 2px solid #e9ecef;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Verificação de dados
# ---------------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def load_all_data():
    """Carrega todos os datasets com cache."""
    return carregar_todos()


def mostrar_erro_dados():
    """Mostra instruções quando os dados não estão disponíveis."""
    status = verificar_dados()
    faltando = [nome for nome, ok in status.items() if not ok]

    st.error("⚠️ Arquivos de dados não encontrados!")
    st.markdown("""
    ### Como resolver

    Coloque os arquivos `.xlsx` na pasta `data/raw/`:

    ```
    data/raw/
    ├── Estabelecimentos_estados.xlsx
    ├── Analise_Estabelecimentos_3rank_municipio_sp.xlsx
    ├── Analise_Funcionarios_3rank_estados.xlsx
    └── Analise_Funcionarios_3rank_municipio_sp.xlsx
    ```

    **Faltando:**
    """)
    for nome in faltando:
        st.markdown(f"- ❌ `{nome}`")

    st.info("💡 Os dados originais vêm da RAIS (Relação Anual de Informações Sociais) do Ministério do Trabalho.")
    st.stop()


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

def sidebar(datasets: dict[str, Dataset]) -> tuple[str, Dataset, list[str], str]:
    """Renderiza a sidebar e retorna as seleções do usuário."""

    with st.sidebar:
        st.markdown("## 🔬 Microeletrônica")
        st.markdown("---")

        # Seleção do dataset
        opcoes_dataset = {
            "estab_estados": "📊 Estabelecimentos por Estado",
            "estab_municipios_sp": "📊 Estabelecimentos por Município (SP)",
            "empreg_estados": "👥 Empregados por Estado",
            "empreg_municipios_sp": "👥 Empregados por Município (SP)",
        }

        # Filtra apenas os disponíveis
        opcoes_disponiveis = {
            k: v for k, v in opcoes_dataset.items() if k in datasets
        }

        nome_dataset = st.selectbox(
            "**Dataset**",
            options=list(opcoes_disponiveis.keys()),
            format_func=lambda x: opcoes_disponiveis[x],
        )

        dataset = datasets[nome_dataset]

        st.markdown("---")

        # Filtro de localidades
        st.markdown("**Localidades**")

        todas = st.checkbox("Selecionar todas", value=True)

        if todas:
            localidades_selecionadas = dataset.localidades
        else:
            localidades_selecionadas = st.multiselect(
                "Escolha as localidades:",
                options=dataset.localidades,
                default=dataset.localidades[:3],
            )

        st.markdown("---")

        # Tipo de visualização
        tipo_grafico = st.radio(
            "**Visualização**",
            options=["serie_temporal", "barras_ranking", "heatmap", "variacao"],
            format_func=lambda x: {
                "serie_temporal": "📈 Série Temporal",
                "barras_ranking": "📊 Ranking (Barras)",
                "heatmap": "🗺️ Heatmap Evolução",
                "variacao": "📉 Variação Percentual",
            }[x],
        )

        st.markdown("---")
        st.caption(f"Período: **{dataset.periodo}**")
        st.caption(f"Localidades: **{len(dataset.localidades)}**")

        return nome_dataset, dataset, localidades_selecionadas, tipo_grafico


# ---------------------------------------------------------------------------
# Métricas resumo
# ---------------------------------------------------------------------------

def mostrar_metricas(dataset: Dataset, localidades: list[str]):
    """Exibe cards de métricas no topo."""
    primeiro_ano = dataset.anos[0]
    ultimo_ano = dataset.anos[-1]

    total_inicio = dataset.df.loc[primeiro_ano, localidades].sum()
    total_fim = dataset.df.loc[ultimo_ano, localidades].sum()
    variacao = ((total_fim - total_inicio) / total_inicio * 100) if total_inicio else 0

    # Encontrar o líder
    lider = dataset.df.loc[ultimo_ano, localidades].idxmax()
    valor_lider = dataset.df.loc[ultimo_ano, lider]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label=f"Total ({ultimo_ano})",
            value=f"{total_fim:,.0f}",
        )
    with col2:
        st.metric(
            label=f"Total ({primeiro_ano})",
            value=f"{total_inicio:,.0f}",
        )
    with col3:
        st.metric(
            label=f"Variação {primeiro_ano}→{ultimo_ano}",
            value=f"{variacao:+.1f}%",
            delta=f"{variacao:+.1f}%",
        )
    with col4:
        st.metric(
            label=f"Líder ({ultimo_ano})",
            value=lider,
            delta=f"{valor_lider:,.0f}",
        )


# ---------------------------------------------------------------------------
# Área principal
# ---------------------------------------------------------------------------

def mostrar_grafico(
    dataset: Dataset,
    localidades: list[str],
    tipo: str,
):
    """Renderiza o gráfico selecionado."""

    if not localidades:
        st.warning("Selecione pelo menos uma localidade na barra lateral.")
        return

    if tipo == "serie_temporal":
        fig = charts.serie_temporal(dataset, localidades=localidades)

    elif tipo == "barras_ranking":
        ano = st.select_slider(
            "Selecione o ano",
            options=dataset.anos,
            value=dataset.anos[-1],
        )
        fig = charts.barras_comparativo(
            dataset,
            ano=ano,
            top_n=min(15, len(localidades)),
        )

    elif tipo == "heatmap":
        fig = charts.heatmap_evolucao(
            dataset,
            localidades=localidades[:15],  # limita para legibilidade
        )

    elif tipo == "variacao":
        fig = charts.variacao_percentual(
            dataset,
            localidades=localidades,
            top_n=min(15, len(localidades)),
        )
    else:
        st.error(f"Tipo de gráfico desconhecido: {tipo}")
        return

    st.plotly_chart(fig, use_container_width=True)


def mostrar_tabela(dataset: Dataset, localidades: list[str]):
    """Tabela dos dados brutos com formatação."""
    with st.expander("📋 Ver dados brutos", expanded=False):
        df_exibir = dataset.df[localidades].copy()
        df_exibir.index.name = "Ano"

        st.dataframe(
            df_exibir.style.format("{:,.0f}"),
            use_container_width=True,
            height=400,
        )

        # Botão de download
        csv = df_exibir.to_csv()
        st.download_button(
            label="⬇️ Baixar como CSV",
            data=csv,
            file_name=f"microeletronica_{dataset.nome}.csv",
            mime="text/csv",
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Header
    st.markdown('<p class="main-header">🔬 Microeletrônica no Brasil</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">'
        'Análise temporal do setor de microeletrônica — Estabelecimentos e Empregados (2006–2019)'
        '</p>',
        unsafe_allow_html=True,
    )

    # Carregar dados
    datasets = load_all_data()

    if not datasets:
        mostrar_erro_dados()
        return

    # Sidebar
    nome_dataset, dataset, localidades, tipo_grafico = sidebar(datasets)

    # Descrição
    st.info(f"📌 **{dataset.titulo}** — {dataset.descricao}")

    # Métricas
    if localidades:
        mostrar_metricas(dataset, localidades)

    st.markdown("---")

    # Gráfico
    mostrar_grafico(dataset, localidades, tipo_grafico)

    # Tabela
    if localidades:
        mostrar_tabela(dataset, localidades)

    # Footer
    st.markdown("---")
    st.caption(
        "📚 **Fonte:** RAIS (Relação Anual de Informações Sociais) — "
        "Ministério do Trabalho e Emprego | "
        "**TCC (2021)** — Análise da indústria de microeletrônica no Brasil"
    )


if __name__ == "__main__":
    main()
