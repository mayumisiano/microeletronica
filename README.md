# 🔬 Microeletrônica no Brasil — Análise Temporal

Análise de série temporal dos estados brasileiros e municípios de São Paulo sobre a quantidade de funcionários e estabelecimentos referentes ao ramo da **Microeletrônica**, utilizando Python para gerar séries temporais interativas e observar mudanças no período de **2006 a 2019**.

> **Origem:** TCC apresentado em 2021, analisando a indústria de microeletrônica no Brasil durante a pandemia.

## 📊 O que é analisado?

- **Estabelecimentos** do setor de microeletrônica por estado e por município de São Paulo
- **Empregados** no setor por estado e por município de São Paulo
- 4 tipos de visualização: séries temporais, ranking por barras, heatmap e variação percentual
- Métricas resumo com totais e variação no período

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/mayumisiano/microeletronica.git
cd microeletronica
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Adicione os dados

Coloque os arquivos `.xlsx` na pasta `data/raw/`. Veja detalhes em [`data/README.md`](data/README.md).

### 4. Execute o dashboard

```bash
streamlit run app.py
```

O dashboard abrirá em `http://localhost:8501` com:
- Seleção de dataset (estabelecimentos/empregados × estados/municípios)
- Filtros de localidades
- 4 tipos de gráfico interativo
- Tabela de dados com download em CSV

> 💡 O notebook Jupyter também está disponível para exploração:
> ```bash
> jupyter notebook "Indústria_Microeletrônica_Análise_Temporal.ipynb"
> ```

## 🛠️ Tecnologias

- **Python 3.10+**
- **Pandas** — manipulação e limpeza de dados
- **Plotly** — visualizações interativas
- **Streamlit** — dashboard web interativo

## 📁 Estrutura

```
microeletronica/
├── app.py                # 🚀 Dashboard Streamlit (ponto de entrada)
├── src/
│   ├── __init__.py
│   ├── data_loader.py    # ETL: carregamento e limpeza dos dados
│   └── charts.py         # Gráficos Plotly reutilizáveis
├── data/
│   ├── raw/              # Arquivos .xlsx originais
│   └── README.md         # Documentação das fontes de dados
├── Indústria_Microeletrônica_Análise_Temporal.ipynb  # Notebook (exploração)
├── MELHORIAS.md          # Plano de melhorias e modernização
├── requirements.txt
├── .gitignore
└── README.md
```

## 📈 Melhorias planejadas

Veja o plano completo em [`MELHORIAS.md`](MELHORIAS.md), incluindo:
- Mapas geográficos (choropleth por estado)
- Dados atualizados pós-pandemia (2020–2024)
- Análises estatísticas avançadas (tendências, CAGR)
- Deploy na nuvem (Streamlit Cloud)

## 📝 Fonte dos dados

**RAIS** (Relação Anual de Informações Sociais) — Ministério do Trabalho e Emprego do Brasil.
