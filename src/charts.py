"""
Módulo de visualizações para dados de microeletrônica.

Gera gráficos interativos com Plotly, prontos para uso
no Streamlit, Jupyter ou exportação HTML.
"""

from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from .data_loader import Dataset

# ---------------------------------------------------------------------------
# Paletas e configurações visuais
# ---------------------------------------------------------------------------

COLORS = px.colors.qualitative.Set2
TEMPLATE = "plotly_white"

_LAYOUT_BASE = dict(
    template=TEMPLATE,
    hovermode="x unified",
    height=500,
    margin=dict(l=60, r=30, t=60, b=80),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5,
    ),
)


# ---------------------------------------------------------------------------
# Gráficos
# ---------------------------------------------------------------------------


def serie_temporal(
    dataset: Dataset,
    localidades: list[str] | None = None,
    top_n: int | None = None,
    titulo: str | None = None,
) -> go.Figure:
    """
    Gráfico de linhas — série temporal de uma ou mais localidades.

    Parâmetros:
        dataset: Dataset carregado
        localidades: Subconjunto de localidades a exibir (None = todas)
        top_n: Limitar às N primeiras localidades
        titulo: Título personalizado (usa o do dataset se None)
    """
    cols = localidades or dataset.localidades
    if top_n:
        cols = cols[:top_n]

    titulo = titulo or dataset.titulo

    fig = go.Figure()
    for i, col in enumerate(cols):
        fig.add_trace(go.Scatter(
            x=dataset.df.index,
            y=dataset.df[col],
            mode="lines+markers",
            name=col,
            marker=dict(size=7),
            line=dict(color=COLORS[i % len(COLORS)], width=2.5),
            hovertemplate=(
                f"<b>{col}</b><br>"
                f"Ano: %{{x}}<br>"
                f"{dataset.ylabel}: %{{y:,.0f}}"
                f"<extra></extra>"
            ),
        ))

    fig.update_layout(
        title=dict(text=titulo, font=dict(size=18)),
        xaxis_title="Ano",
        yaxis_title=dataset.ylabel,
        **_LAYOUT_BASE,
    )

    return fig


def barras_comparativo(
    dataset: Dataset,
    ano: str,
    top_n: int = 10,
    titulo: str | None = None,
) -> go.Figure:
    """
    Gráfico de barras horizontais — ranking de localidades em um ano específico.

    Parâmetros:
        dataset: Dataset carregado
        ano: Ano para o ranking (ex: '2019')
        top_n: Número de localidades no ranking
        titulo: Título personalizado
    """
    if ano not in dataset.df.index:
        raise ValueError(f"Ano '{ano}' não encontrado. Disponíveis: {dataset.anos}")

    dados_ano = dataset.df.loc[ano].dropna().sort_values(ascending=True)
    dados_top = dados_ano.tail(top_n)

    titulo = titulo or f"{dataset.titulo} — Ranking {ano}"

    fig = go.Figure(go.Bar(
        x=dados_top.values,
        y=dados_top.index,
        orientation="h",
        marker_color=COLORS[0],
        hovertemplate=(
            "<b>%{y}</b><br>"
            f"{dataset.ylabel}: %{{x:,.0f}}"
            "<extra></extra>"
        ),
    ))

    fig.update_layout(
        title=dict(text=titulo, font=dict(size=18)),
        xaxis_title=dataset.ylabel,
        yaxis_title="",
        **_LAYOUT_BASE,
    )

    return fig


def heatmap_evolucao(
    dataset: Dataset,
    localidades: list[str] | None = None,
    top_n: int = 10,
    titulo: str | None = None,
) -> go.Figure:
    """
    Heatmap — evolução ao longo dos anos por localidade.

    Parâmetros:
        dataset: Dataset carregado
        localidades: Subconjunto de localidades (None = top_n por último ano)
        top_n: Se localidades=None, usa as top_n do último ano
        titulo: Título personalizado
    """
    if localidades:
        cols = localidades
    else:
        ultimo_ano = dataset.df.index[-1]
        cols = (
            dataset.df.loc[ultimo_ano]
            .dropna()
            .sort_values(ascending=False)
            .head(top_n)
            .index.tolist()
        )

    df_subset = dataset.df[cols].T

    titulo = titulo or f"{dataset.titulo} — Evolução Temporal"

    fig = go.Figure(go.Heatmap(
        z=df_subset.values,
        x=df_subset.columns,
        y=df_subset.index,
        colorscale="YlOrRd",
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Ano: %{x}<br>"
            f"{dataset.ylabel}: %{{z:,.0f}}"
            "<extra></extra>"
        ),
    ))

    fig.update_layout(
        title=dict(text=titulo, font=dict(size=18)),
        xaxis_title="Ano",
        yaxis_title="",
        **_LAYOUT_BASE,
        height=max(400, len(cols) * 35),
    )

    return fig


def variacao_percentual(
    dataset: Dataset,
    localidades: list[str] | None = None,
    top_n: int = 5,
    titulo: str | None = None,
) -> go.Figure:
    """
    Gráfico de barras — variação percentual entre o primeiro e o último ano.

    Parâmetros:
        dataset: Dataset carregado
        localidades: Subconjunto de localidades
        top_n: Número de localidades a exibir
        titulo: Título personalizado
    """
    primeiro = dataset.df.index[0]
    ultimo = dataset.df.index[-1]

    inicio = dataset.df.loc[primeiro]
    fim = dataset.df.loc[ultimo]

    variacao = ((fim - inicio) / inicio * 100).dropna().sort_values(ascending=True)

    if localidades:
        variacao = variacao[variacao.index.isin(localidades)]

    # Pega os top_n maiores e menores
    top = variacao.tail(top_n)

    titulo = titulo or f"{dataset.titulo} — Variação {primeiro}→{ultimo} (%)"

    cores = [COLORS[2] if v >= 0 else COLORS[5] for v in top.values]

    fig = go.Figure(go.Bar(
        x=top.values,
        y=top.index,
        orientation="h",
        marker_color=cores,
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Variação: %{x:+.1f}%"
            "<extra></extra>"
        ),
    ))

    fig.update_layout(
        title=dict(text=titulo, font=dict(size=18)),
        xaxis_title="Variação (%)",
        yaxis_title="",
        **_LAYOUT_BASE,
    )

    return fig
