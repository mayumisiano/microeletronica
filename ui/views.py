import streamlit as st

from src import charts
from src.data_loader import Dataset, check_data


def show_missing_data() -> None:
    """Display an error message when data files are not found."""
    status = check_data()
    missing = [name for name, ok in status.items() if not ok]

    st.error("⚠️ Arquivos de dados não encontrados!")
    st.markdown("""
    ### Como resolver

    Coloque os arquivos `.xlsx` na pasta `data/`:

    ```
    data/
    ├── estabelecimentos_estados.xlsx
    ├── estabelecimentos_municipios_sp.xlsx
    ├── empregados_estados.xlsx
    └── empregados_municipios_sp.xlsx
    ```

    **Faltando:**
    """)
    for name in missing:
        st.markdown(f"- ❌ `{name}`")

    st.info(
        "💡 Dados originais da RAIS (Relação Anual de Informações Sociais) "
        "— Ministério do Trabalho e Emprego."
    )
    st.stop()


def show_metrics(dataset: Dataset, localities: list[str], top_n: int | None = None) -> None:
    """Display summary metric cards at the top of the page."""
    first_year = dataset.years[0]
    last_year = dataset.years[-1]

    if top_n:
        ranked = dataset.df.loc[last_year, localities].dropna().sort_values(ascending=False)
        localities = ranked.head(top_n).index.tolist()

    total_start = dataset.df.loc[first_year, localities].sum()
    total_end = dataset.df.loc[last_year, localities].sum()
    change = ((total_end - total_start) / total_start * 100) if total_start else 0

    leader = dataset.df.loc[last_year, localities].idxmax()
    leader_value = dataset.df.loc[last_year, leader]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label=f"Total ({last_year})", value=f"{total_end:,.0f}")
    with col2:
        st.metric(label=f"Total ({first_year})", value=f"{total_start:,.0f}")
    with col3:
        st.metric(
            label=f"Variação {first_year}→{last_year}",
            value=f"{change:+.1f}%",
            delta=f"{change:+.1f}%",
        )
    with col4:
        st.metric(
            label=f"Líder ({last_year})",
            value=leader,
            delta=f"{leader_value:,.0f}",
        )


def show_chart(
    dataset: Dataset,
    localities: list[str],
    chart_type: str,
    top_n: int | None = None,
) -> None:
    """Render the selected chart type."""
    if not localities:
        st.warning("Selecione pelo menos uma localidade na barra lateral.")
        return

    if chart_type == "time_series":
        fig = charts.time_series(dataset, localities=localities, top_n=top_n)

    elif chart_type == "bar_ranking":
        year = st.select_slider(
            "Selecione o ano",
            options=dataset.years,
            value=dataset.years[-1],
        )
        fig = charts.bar_ranking(
            dataset,
            year=year,
            top_n=top_n or min(15, len(localities)),
        )

    elif chart_type == "heatmap":
        fig = charts.heatmap_evolution(
            dataset,
            localities=localities,
            top_n=top_n or 15,
        )

    elif chart_type == "pct_change":
        fig = charts.pct_change(
            dataset,
            localities=localities,
            top_n=top_n or min(15, len(localities)),
        )
    else:
        st.error(f"Tipo de gráfico desconhecido: {chart_type}")
        return

    st.plotly_chart(fig, use_container_width=True)


def show_table(dataset: Dataset, localities: list[str]) -> None:
    """Expandable raw data table with CSV download."""
    with st.expander("📋 Dados brutos", expanded=False):
        df_display = dataset.df[localities].copy()
        df_display.index.name = "Ano"

        st.dataframe(
            df_display.style.format("{:,.0f}"),
            use_container_width=True,
            height=400,
        )

        csv = df_display.to_csv()
        st.download_button(
            label="⬇️ Baixar CSV",
            data=csv,
            file_name=f"microeletronica_{dataset.name}.csv",
            mime="text/csv",
        )
