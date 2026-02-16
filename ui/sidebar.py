import streamlit as st

from src.data_loader import Dataset

DATASET_OPTIONS = {
    "estab_estados": "📊 Estabelecimentos por Estado",
    "estab_municipios_sp": "📊 Estabelecimentos por Município (SP)",
    "empreg_estados": "👥 Empregados por Estado",
    "empreg_municipios_sp": "👥 Empregados por Município (SP)",
}


def render(
    datasets: dict[str, Dataset],
) -> tuple[str, Dataset, list[str], str, int | None]:
    """Render sidebar controls and return the user's selections."""
    with st.sidebar:
        st.markdown("## 🔬 Microeletrônica")
        st.markdown("---")

        available = {k: v for k, v in DATASET_OPTIONS.items() if k in datasets}

        dataset_key = st.selectbox(
            "**Dataset**",
            options=list(available.keys()),
            format_func=lambda x: available[x],
        )

        dataset = datasets[dataset_key]
        total = len(dataset.localities)

        st.markdown("---")
        st.markdown("**Localidades**")

        mode = st.radio(
            "Filtro",
            options=["top_n", "manual"],
            format_func=lambda x: {
                "top_n": f"Top N (de {total})",
                "manual": "Escolher manualmente",
            }[x],
            label_visibility="collapsed",
        )

        if mode == "top_n":
            default_n = min(10, total)
            top_n = st.slider(
                "Quantidade",
                min_value=1,
                max_value=total,
                value=default_n,
            )
            selected_localities = dataset.localities
        else:
            top_n = None
            selected_localities = st.multiselect(
                "Escolha as localidades:",
                options=dataset.localities,
                default=dataset.localities[:5],
            )

        st.markdown("---")

        chart_type = st.radio(
            "**Visualização**",
            options=["time_series", "bar_ranking", "heatmap", "pct_change"],
            format_func=lambda x: {
                "time_series": "📈 Série Temporal",
                "bar_ranking": "📊 Ranking (Barras)",
                "heatmap": "🗺️ Heatmap Evolução",
                "pct_change": "📉 Variação Percentual",
            }[x],
        )

        st.markdown("---")
        st.caption(f"Período: **{dataset.period}**")
        st.caption(f"Localidades: **{total}** no total")

        return dataset_key, dataset, selected_localities, chart_type, top_n
