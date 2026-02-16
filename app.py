import streamlit as st

from src.data_loader import load_all
from ui.style import PAGE_CONFIG, inject_css
from ui.sidebar import render as render_sidebar
from ui.views import show_missing_data, show_metrics, show_chart, show_table

st.set_page_config(**PAGE_CONFIG)
inject_css()


@st.cache_data(show_spinner=False)
def cached_load_all():
    return load_all()


def main():
    st.markdown(
        '<p class="main-header">🔬 Microeletrônica no Brasil</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-header">'
        "Análise temporal da indústria de microeletrônica — "
        "Estabelecimentos e Empregados (2006–2019)"
        "</p>",
        unsafe_allow_html=True,
    )

    datasets = cached_load_all()

    if not datasets:
        show_missing_data()
        return

    dataset_key, dataset, localities, chart_type, top_n = render_sidebar(datasets)

    st.info(f"📌 **{dataset.title}** — {dataset.description}")

    if localities:
        show_metrics(dataset, localities, top_n)

    st.markdown("---")

    show_chart(dataset, localities, chart_type, top_n)

    if localities:
        show_table(dataset, localities)

    st.markdown("---")
    st.caption(
        "📚 **Fonte:** RAIS (Relação Anual de Informações Sociais) — "
        "Ministério do Trabalho e Emprego | "
        "**TCC (2021)** — Análise da indústria de microeletrônica no Brasil"
    )


if __name__ == "__main__":
    main()
