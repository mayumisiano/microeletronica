# 🗺️ Roadmap

Planned improvements and modernization phases for the microelectronics analysis project

---

## Phase 1 — Data Expansion

- [ ] Include post-2019 data (pandemic period) — source: RAIS/CAGED
- [ ] Add data from other CNAE subclasses related to microelectronics
- [ ] Automate data download/update pipeline

## Phase 2 — Advanced Visualizations

- [ ] Geographic choropleth maps (by state and municipality)
- [ ] Animated time series (year-by-year playback)
- [ ] Correlation charts (establishments × employees)

## Phase 3 — Statistical Analysis

- [ ] Compound Annual Growth Rate (CAGR) per locality
- [ ] Trend analysis and forecasting
- [ ] Concentration indices (HHI, Gini)
- [ ] Pre/post pandemic comparative analysis

## Phase 4 — Infrastructure

- [ ] Deploy to Streamlit Cloud
- [ ] CI/CD with GitHub Actions (lint, format, tests)
- [ ] Add unit tests for `src/data_loader.py` and `src/charts.py`
- [ ] Containerize with Docker

## Phase 5 — Context & Storytelling

- [ ] Annotate charts with industry events (chip crisis, pandemic, policy changes)
- [ ] Add narrative sections explaining trends
- [ ] Compare with global microelectronics data
