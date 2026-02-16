from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go

from .data_loader import Dataset

COLORS = px.colors.qualitative.Set2
TEMPLATE = "plotly_white"

_BASE_LAYOUT = dict(
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


def time_series(
    dataset: Dataset,
    localities: list[str] | None = None,
    top_n: int | None = None,
    title: str | None = None,
) -> go.Figure:
    """Line chart showing one or more localities over time."""
    cols = localities or dataset.localities
    if top_n and top_n < len(cols):
        last_year = dataset.df.index[-1]
        ranked = dataset.df.loc[last_year, cols].dropna().sort_values(ascending=False)
        cols = ranked.head(top_n).index.tolist()

    title = title or dataset.title

    fig = go.Figure()
    for i, col in enumerate(cols):
        fig.add_trace(
            go.Scatter(
                x=dataset.df.index,
                y=dataset.df[col],
                mode="lines+markers",
                name=col,
                marker=dict(size=7),
                line=dict(color=COLORS[i % len(COLORS)], width=2.5),
                hovertemplate=(
                    f"<b>{col}</b><br>Ano: %{{x}}<br>{dataset.ylabel}: %{{y:,.0f}}<extra></extra>"
                ),
            )
        )

    fig.update_layout(
        title=dict(text=title, font=dict(size=18)),
        xaxis_title="Ano",
        yaxis_title=dataset.ylabel,
        **_BASE_LAYOUT,
    )

    return fig


def bar_ranking(
    dataset: Dataset,
    year: str,
    top_n: int = 10,
    title: str | None = None,
) -> go.Figure:
    """Horizontal bar chart ranking localities for a given year."""
    if year not in dataset.df.index:
        raise ValueError(f"Year '{year}' not found. Available: {dataset.years}")

    year_data = dataset.df.loc[year].dropna().sort_values(ascending=True)
    top_data = year_data.tail(top_n)

    title = title or f"{dataset.title} — Ranking {year}"

    fig = go.Figure(
        go.Bar(
            x=top_data.values,
            y=top_data.index,
            orientation="h",
            marker_color=COLORS[0],
            hovertemplate=(f"<b>%{{y}}</b><br>{dataset.ylabel}: %{{x:,.0f}}<extra></extra>"),
        )
    )

    fig.update_layout(
        title=dict(text=title, font=dict(size=18)),
        xaxis_title=dataset.ylabel,
        yaxis_title="",
        **_BASE_LAYOUT,
    )

    return fig


def heatmap_evolution(
    dataset: Dataset,
    localities: list[str] | None = None,
    top_n: int = 10,
    title: str | None = None,
) -> go.Figure:
    """Heatmap of values across years and localities."""
    if localities:
        cols = localities
    else:
        last_year = dataset.df.index[-1]
        cols = (
            dataset.df.loc[last_year]
            .dropna()
            .sort_values(ascending=False)
            .head(top_n)
            .index.tolist()
        )

    df_subset = dataset.df[cols].T

    title = title or f"{dataset.title} — Evolução Temporal"

    fig = go.Figure(
        go.Heatmap(
            z=df_subset.values,
            x=df_subset.columns,
            y=df_subset.index,
            colorscale="YlOrRd",
            hovertemplate=(
                f"<b>%{{y}}</b><br>Ano: %{{x}}<br>{dataset.ylabel}: %{{z:,.0f}}<extra></extra>"
            ),
        )
    )

    fig.update_layout(
        **{**_BASE_LAYOUT, "height": max(400, len(cols) * 35)},
        title=dict(text=title, font=dict(size=18)),
        xaxis_title="Ano",
        yaxis_title="",
    )

    return fig


def pct_change(
    dataset: Dataset,
    localities: list[str] | None = None,
    top_n: int = 5,
    title: str | None = None,
) -> go.Figure:
    """Horizontal bar chart showing percentage change between first and last year."""
    first = dataset.df.index[0]
    last = dataset.df.index[-1]

    start = dataset.df.loc[first]
    end = dataset.df.loc[last]

    change = ((end - start) / start * 100).dropna().sort_values(ascending=True)

    if localities:
        change = change[change.index.isin(localities)]

    top = change.tail(top_n)

    title = title or f"{dataset.title} — Variação {first}→{last} (%)"

    bar_colors = [COLORS[2] if v >= 0 else COLORS[5] for v in top.values]

    fig = go.Figure(
        go.Bar(
            x=top.values,
            y=top.index,
            orientation="h",
            marker_color=bar_colors,
            hovertemplate=("<b>%{y}</b><br>Variação: %{x:+.1f}%<extra></extra>"),
        )
    )

    fig.update_layout(
        title=dict(text=title, font=dict(size=18)),
        xaxis_title="Variação (%)",
        yaxis_title="",
        **_BASE_LAYOUT,
    )

    return fig


# backward-compat aliases (notebook)
serie_temporal = time_series
barras_comparativo = bar_ranking
heatmap_evolucao = heatmap_evolution
variacao_percentual = pct_change
