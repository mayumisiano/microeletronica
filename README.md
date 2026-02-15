# 🔬 Microeletrônica no Brasil — Análise Temporal

Análise de série temporal dos estados brasileiros e municípios de São Paulo sobre a quantidade de funcionários e estabelecimentos referentes ao ramo da **Microeletrônica**, utilizando Python para gerar séries temporais interativas e observar mudanças no período de **2006 a 2019**.

> **Origem:** TCC apresentado em 2021, analisando a indústria de microeletrônica no Brasil durante a pandemia.

## 📊 O que é analisado?

- **Estabelecimentos** do setor de microeletrônica por estado e por município de São Paulo
- **Empregados** no setor por estado e por município de São Paulo
- Séries temporais com gráficos interativos (Plotly)

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

### 4. Execute o notebook

```bash
jupyter notebook "Indústria_Microeletrônica_Análise_Temporal.ipynb"
```

## 🛠️ Tecnologias

- **Python 3.10+**
- **Pandas** — manipulação de dados
- **Plotly** — visualizações interativas
- **Jupyter** — ambiente de análise

## 📁 Estrutura

```
microeletronica/
├── data/
│   ├── raw/              # Arquivos .xlsx originais
│   └── README.md         # Documentação das fontes de dados
├── Indústria_Microeletrônica_Análise_Temporal.ipynb  # Notebook principal
├── MELHORIAS.md          # Plano de melhorias e modernização
├── requirements.txt
├── .gitignore
└── README.md
```

## 📈 Melhorias planejadas

Veja o plano completo em [`MELHORIAS.md`](MELHORIAS.md), incluindo:
- Dashboard interativo com Streamlit
- Mapas geográficos por estado
- Dados atualizados pós-pandemia
- Análises estatísticas (tendências, CAGR)

## 📝 Fonte dos dados

**RAIS** (Relação Anual de Informações Sociais) — Ministério do Trabalho e Emprego do Brasil.
