<a id="top"></a>
<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/🇧🇷_Português-30363d?style=for-the-badge" alt="Português"/></a>
<a href="README.en.md"><img src="https://img.shields.io/badge/🇺🇸_English-58a6ff?style=for-the-badge" alt="English"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:30363d&height=220&section=header&text=Microelectronics%20%F0%9F%94%AC&fontSize=42&fontColor=58a6ff&fontAlignY=35&desc=Time%20series%20analysis%20of%20Brazil's%20industry%20(2006%E2%80%932019)&descSize=16&descColor=8b949e&descAlignY=55&animation=fadeIn" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&repeat=true&width=500&height=30&lines=Time+series+%E2%80%A2+2006%E2%80%932019;Interactive+dashboards+with+Streamlit;Visualizations+with+Plotly;RAIS+data+%E2%80%A2+Microelectronics+%F0%9F%87%A7%F0%9F%87%B7" alt="Typing SVG" />
</a>

<br/>

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=ffd43b)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.24+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2+-150458?style=for-the-badge&logo=pandas&logoColor=white)
![uv](https://img.shields.io/badge/uv-package_manager-DE5FE9?style=for-the-badge&logo=uv&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-linter-D7FF64?style=for-the-badge&logo=ruff&logoColor=261230)

<br/>

![Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmayumisiano%2Fmicroeletronica%2Fmain%2Fpyproject.toml&query=%24.project.version&style=flat-square&label=version&color=30363d&labelColor=0d1117)
![License](https://img.shields.io/github/license/mayumisiano/microeletronica?style=flat-square&color=30363d&labelColor=0d1117)
![Last Commit](https://img.shields.io/github/last-commit/mayumisiano/microeletronica?style=flat-square&color=30363d&labelColor=0d1117)
![Repo Size](https://img.shields.io/github/repo-size/mayumisiano/microeletronica?style=flat-square&color=30363d&labelColor=0d1117)
![Visitor Count](https://komarev.com/ghpvc/?username=mayumisiano-microeletronica&style=flat-square&color=30363d&label=visitors)

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## About

> Time series analysis of Brazilian states and São Paulo municipalities regarding the **number of employees and establishments** in the **Microelectronics** industry, generating interactive visualizations for the **2006–2019** period.
>
> **Origin:** Undergraduate thesis (TCC) presented in 2021, analyzing Brazil's microelectronics industry during the pandemic.

<br/>

<div align="center">
<table>
<tr>
<td align="center">

**What is analyzed**

```
 📊 Establishments (by state and SP municipality)
 👥 Employees (by state and SP municipality)
 📈 4 visualization types
 📋 Summary metrics and percentage change
```

</td>
<td align="center">

**Distribution example (illustrative)**

<img src="https://quickchart.io/chart?c={type:'doughnut',data:{labels:['SP','RJ','MG','RS','Others'],datasets:[{data:[45,20,12,8,15],backgroundColor:['%2358a6ff','%23bc8cff','%2339d353','%23f0883e','%238b949e']}]},options:{plugins:{legend:{labels:{color:'%23c9d1d9'}},doughnutlabel:{labels:[{text:'States',font:{size:14},color:'%23c9d1d9'}]}},layout:{padding:10}}}&backgroundColor=%230d1117&width=280&height=200" alt="chart"/>

</td>
</tr>
</table>
</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Quick Start

<details open>
<summary><b>Setup in 3 steps</b></summary>
<br/>

**1.** Clone the repository

```bash
git clone https://github.com/mayumisiano/microeletronica.git && cd microeletronica
```

**2.** Install dependencies

```bash
uv sync
```

**3.** Place the `.xlsx` files in `data/raw/` — see [`data/README.md`](data/README.md)

</details>

<details open>
<summary><b>Available commands</b></summary>
<br/>

| Command | Description |
|:--|:--|
| `uv run task dev` | Start Streamlit dashboard |
| `uv run task notebook` | Open Jupyter Notebook |
| `uv run task lint` | Run Ruff linter |
| `uv run task format` | Auto-format code |
| `uv run task check` | Lint + format check (CI) |

> The dashboard opens at `http://localhost:8501` with interactive filters, 4 chart types, and CSV download.

</details>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Tech Stack

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,anaconda,github,vscode&theme=dark&perline=8" alt="Tech Stack Icons"/>
  </a>
</div>

<br/>

<div align="center">
<table>
<tr>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="40" height="40" alt="Pandas"/>
<br/><sub><b>Pandas</b></sub>
<br/><sub><sup>ETL & Data</sup></sub>
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/plotly/plotly-original.svg" width="40" height="40" alt="Plotly"/>
<br/><sub><b>Plotly</b></sub>
<br/><sub><sup>Visualizations</sup></sub>
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" width="40" height="40" alt="Streamlit"/>
<br/><sub><b>Streamlit</b></sub>
<br/><sub><sup>Dashboard</sup></sub>
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="40" height="40" alt="Jupyter"/>
<br/><sub><b>Jupyter</b></sub>
<br/><sub><sup>Exploration</sup></sub>
</td>
<td align="center" width="120">
<img src="https://avatars.githubusercontent.com/u/115962839?s=200&v=4" width="40" height="40" alt="Ruff" style="border-radius:8px"/>
<br/><sub><b>Ruff</b></sub>
<br/><sub><sup>Lint & Format</sup></sub>
</td>
<td align="center" width="120">
<img src="https://avatars.githubusercontent.com/u/142288570?s=200&v=4" width="40" height="40" alt="uv" style="border-radius:8px"/>
<br/><sub><b>uv</b></sub>
<br/><sub><sup>Dependencies</sup></sub>
</td>
</tr>
</table>
</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Structure

```
microeletronica/
│
├── app.py                  ← Streamlit dashboard entry point
│
├── ui/
│   ├── style.py               ← CSS and page configuration
│   ├── sidebar.py             ← Sidebar controls
│   └── views.py               ← Metrics, charts, and data table
│
├── src/
│   ├── data_loader.py         ← ETL: data loading and cleaning
│   └── charts.py              ← Reusable Plotly chart functions
│
├── data/
│   └── raw/
│       └── *.xlsx             ← Raw data (RAIS)
│
├── exploration.ipynb       ← Exploratory notebook
├── pyproject.toml          ← Dependencies and config (uv / ruff)
├── ROADMAP.md              ← Future improvements
└── .gitignore
```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Roadmap

| Feature | Progress |
|:--|:--|
| Interactive Streamlit dashboard | ![100%](https://progress-bar.xyz/100/?title=done&color=39d353&width=120) |
| Exploratory notebook | ![100%](https://progress-bar.xyz/100/?title=done&color=39d353&width=120) |
| Geographic maps (choropleth) | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |
| Post-pandemic data (2020–2024) | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |
| Advanced statistical analysis | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |
| Cloud deployment | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |

> See the full plan in [`ROADMAP.md`](ROADMAP.md)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Data

> [!NOTE]
> **Data source:** RAIS (Relação Anual de Informações Sociais) — Brazilian Ministry of Labor and Employment.

> [!TIP]
> Place the `.xlsx` files in the `data/raw/` folder before running the project. See details in [`data/README.md`](data/README.md).

> [!IMPORTANT]
> Raw data files are not included in the repository due to size constraints. Refer to the documentation to obtain them.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

<div align="center">

## Repository activity

<sub>

**[⬆ Back to top](#top)**

</sub>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:30363d&height=120&section=footer" width="100%"/>
