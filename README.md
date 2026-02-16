# 🔬 Microelectronics in Brazil — Time Series Analysis

Time series analysis of Brazilian states and São Paulo municipalities regarding the number of employees and establishments in the **Microelectronics** industry, using Python to generate interactive visualizations and observe changes over the **2006–2019** period.

> **Origin:** Undergraduate thesis (TCC) presented in 2021, analyzing Brazil's microelectronics industry during the pandemic. 

## What is analyzed?

- **Establishments** in the microelectronics sector by state and by São Paulo municipality
- **Employees** in the sector by state and by São Paulo municipality
- 4 visualization types: time series, bar ranking, heatmap, and percentage change
- Summary metrics with totals and variation over the period

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/mayumisiano/microeletronica.git
cd microeletronica
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Add the data

Place the `.xlsx` files in the `data/raw/` folder. See details in [`data/README.md`](data/README.md).

### 4. Run

All commands use [taskipy](https://github.com/taskipy/taskipy) — defined in `pyproject.toml`:

```bash
uv run task dev        # start Streamlit dashboard
uv run task notebook   # open Jupyter notebook
uv run task lint       # run Ruff linter
uv run task format     # auto-format code
uv run task check      # lint + format check (CI)
```

The dashboard will open at `http://localhost:8501` with:
- Dataset selector (establishments/employees x states/municipalities)
- Locality filters (Top N or manual selection)
- 4 interactive chart types
- Raw data table with CSV download

## Tech stack

- **Python 3.12+**
- **uv** — dependency and virtual environment management
- **Pandas** — data manipulation and cleaning
- **Plotly** — interactive visualizations
- **Streamlit** — interactive web dashboard
- **Ruff** — linter and formatter

## Architecture

The project follows a modular architecture where the **notebook** and the **dashboard** share the same codebase:

```
src/
    data_loader.py   ← ETL (Excel loading and cleaning)
    charts.py        ← Plotly charts

        ↑ imports              ↑ imports
        │                      │
    ┌───┴──────────┐   ┌───────┴───────────┐
    │   Jupyter    │   │    Streamlit      │
    │  (notebook)  │   │   (dashboard)     │
    │              │   │                   │
    │  academic    │   │  app.py + ui/     │
    │  exploration │   │  presentation     │
    └──────────────┘   └──────────────────-┘
```

All ETL and visualization logic lives in `src/` — fix a bug once, and the fix applies to both consumers automatically.

## Structure

```
microeletronica/
├── app.py                 # Dashboard Streamlit entry point
├── ui/
│   ├── style.py           # CSS and page configuration
│   ├── sidebar.py         # Sidebar controls
│   └── views.py           # Metrics, charts, and data table
├── src/
│   ├── data_loader.py     # ETL: data loading and cleaning
│   └── charts.py          # Reusable Plotly chart functions
├── data/
│   └── raw/
│       └── *.xlsx         # Raw data files (RAIS)
├── exploration.ipynb      # Exploratory notebook
├── pyproject.toml         # Dependencies and config (uv / ruff)
├── ROADMAP.md             # Future improvements roadmap
└── .gitignore
```

## Planned improvements

See the full plan in [`ROADMAP.md`](ROADMAP.md), including:
- Geographic maps (choropleth by state)
- Updated post-pandemic data (2020–2024)
- Advanced statistical analysis (trends, CAGR)
- Cloud deployment (Streamlit Cloud)

## Data source

**RAIS** (Relação Anual de Informações Sociais) — Brazilian Ministry of Labor and Employment.
