<a id="top"></a>
<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/🇧🇷_Português-58a6ff?style=for-the-badge" alt="Português"/></a>
<a href="README.en.md"><img src="https://img.shields.io/badge/🇺🇸_English-30363d?style=for-the-badge" alt="English"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:30363d&height=220&section=header&text=Microeletr%C3%B4nica%20%F0%9F%94%AC&fontSize=42&fontColor=58a6ff&fontAlignY=35&desc=An%C3%A1lise%20temporal%20da%20ind%C3%BAstria%20no%20Brasil%20(2006%E2%80%932019)&descSize=16&descColor=8b949e&descAlignY=55&animation=fadeIn" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&repeat=true&width=500&height=30&lines=S%C3%A9ries+temporais+%E2%80%A2+2006%E2%80%932019;Dashboards+interativos+com+Streamlit;Visualiza%C3%A7%C3%B5es+com+Plotly;Dados+RAIS+%E2%80%A2+Microeletr%C3%B4nica+%F0%9F%87%A7%F0%9F%87%B7" alt="Typing SVG" />
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

## Sobre

> Análise de séries temporais dos estados brasileiros e municípios paulistas sobre **número de empregados e estabelecimentos** na indústria de **Microeletrônica**, gerando visualizações interativas para o período **2006–2019**.
>
> **Origem:** TCC (Trabalho de Conclusão de Curso) apresentado em 2021, analisando a indústria de microeletrônica brasileira durante a pandemia.

<br/>

<div align="center">
<table>
<tr>
<td align="center">

**O que é analisado**

```
 📊 Estabelecimentos (por estado e município SP)
 👥 Empregados (por estado e município SP)
 📈 4 tipos de visualização
 📋 Métricas e variação percentual
```

</td>
<td align="center">

**Exemplo de distribuição (ilustrativo)**

<img src="https://quickchart.io/chart?c={type:'doughnut',data:{labels:['SP','RJ','MG','RS','Outros'],datasets:[{data:[45,20,12,8,15],backgroundColor:['%2358a6ff','%23bc8cff','%2339d353','%23f0883e','%238b949e']}]},options:{plugins:{legend:{labels:{color:'%23c9d1d9'}},doughnutlabel:{labels:[{text:'Estados',font:{size:14},color:'%23c9d1d9'}]}},layout:{padding:10}}}&backgroundColor=%230d1117&width=280&height=200" alt="chart"/>

</td>
</tr>
</table>
</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Quick Start

<details open>
<summary><b>Instalação em 3 passos</b></summary>
<br/>

**1.** Clone o repositório

```bash
git clone https://github.com/mayumisiano/microeletronica.git && cd microeletronica
```

**2.** Instale as dependências

```bash
uv sync
```

**3.** Coloque os arquivos `.xlsx` em `data/raw/` — veja [`data/README.md`](data/README.md)

</details>

<details open>
<summary><b>Comandos disponíveis</b></summary>
<br/>

| Comando | Descrição |
|:--|:--|
| `uv run task dev` | Inicia o dashboard Streamlit |
| `uv run task notebook` | Abre o Jupyter Notebook |
| `uv run task lint` | Roda o linter Ruff |
| `uv run task format` | Auto-formata o código |
| `uv run task check` | Lint + format check (CI) |

> O dashboard abre em `http://localhost:8501` com filtros interativos, 4 tipos de gráfico e download de CSV.

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
<br/><sub><sup>ETL & Dados</sup></sub>
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/plotly/plotly-original.svg" width="40" height="40" alt="Plotly"/>
<br/><sub><b>Plotly</b></sub>
<br/><sub><sup>Visualizações</sup></sub>
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" width="40" height="40" alt="Streamlit"/>
<br/><sub><b>Streamlit</b></sub>
<br/><sub><sup>Dashboard</sup></sub>
</td>
<td align="center" width="120">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="40" height="40" alt="Jupyter"/>
<br/><sub><b>Jupyter</b></sub>
<br/><sub><sup>Exploração</sup></sub>
</td>
<td align="center" width="120">
<img src="https://avatars.githubusercontent.com/u/115962839?s=200&v=4" width="40" height="40" alt="Ruff" style="border-radius:8px"/>
<br/><sub><b>Ruff</b></sub>
<br/><sub><sup>Lint & Format</sup></sub>
</td>
<td align="center" width="120">
<img src="https://avatars.githubusercontent.com/u/142288570?s=200&v=4" width="40" height="40" alt="uv" style="border-radius:8px"/>
<br/><sub><b>uv</b></sub>
<br/><sub><sup>Dependências</sup></sub>
</td>
</tr>
</table>
</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Estrutura

```
microeletronica/
│
├── app.py                  ← Entry point do dashboard Streamlit
│
├── ui/
│   ├── style.py               ← CSS e configuração de página
│   ├── sidebar.py             ← Controles da sidebar
│   └── views.py               ← Métricas, gráficos e tabela
│
├── src/
│   ├── data_loader.py         ← ETL: carga e limpeza de dados
│   └── charts.py              ← Funções de gráficos Plotly reutilizáveis
│
├── data/
│   └── raw/
│       └── *.xlsx             ← Dados brutos (RAIS)
│
├── exploration.ipynb       ← Notebook exploratório
├── pyproject.toml          ← Dependências e config (uv / ruff)
├── ROADMAP.md              ← Melhorias futuras
└── .gitignore
```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Roadmap

| Feature | Progresso |
|:--|:--|
| Dashboard interativo Streamlit | ![100%](https://progress-bar.xyz/100/?title=done&color=39d353&width=120) |
| Notebook exploratório | ![100%](https://progress-bar.xyz/100/?title=done&color=39d353&width=120) |
| Mapas geográficos (choropleth) | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |
| Dados pós-pandemia (2020–2024) | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |
| Análise estatística avançada | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |
| Deploy na nuvem | ![0%](https://progress-bar.xyz/0/?title=planned&color=8b949e&width=120) |

> Veja o plano completo em [`ROADMAP.md`](ROADMAP.md)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

## Dados

> [!NOTE]
> **Fonte dos dados:** RAIS (Relação Anual de Informações Sociais) — Ministério do Trabalho e Emprego do Brasil.

> [!TIP]
> Coloque os arquivos `.xlsx` na pasta `data/raw/` antes de rodar o projeto. Veja detalhes em [`data/README.md`](data/README.md).

> [!IMPORTANT]
> Os dados brutos não estão incluídos no repositório por questões de tamanho. Consulte a documentação para obtê-los.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%"/>

<div align="center">

<sub>

**[⬆ Voltar ao topo](#top)**

</sub>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:30363d&height=120&section=footer" width="100%"/>
