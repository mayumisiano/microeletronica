# 🔬 Plano de Melhorias — Microeletrônica no Brasil

> Documento de análise e proposta de modernização do TCC de 2021 sobre a indústria de microeletrônica no Brasil.

---

## 📋 Resumo do Estado Atual

O projeto original consiste em um notebook Google Colab que analisa dados de estabelecimentos e empregados do setor de microeletrônica no Brasil, com séries temporais por estado e municípios de São Paulo (período 2006–2019). Os dados vêm de arquivos Excel (`.xlsx`) que são carregados via upload manual no Colab.

---

## 🐛 Bugs Encontrados

### 1. Label do eixo Y incorreto nos gráficos de empregados
- **Célula 17** (Empregados por Estado): `plt.ylabel('Estabelecimentos')` → deveria ser `'Empregados'`
- **Célula 20** (Empregados por Município): Mesmo erro — label diz "Estabelecimentos" mas exibe dados de empregados

### 2. Labels hardcoded podem não corresponder aos dados
- As legendas são escritas manualmente (`labels = ["São Paulo", "Amazonas", "Minas Gerais"]`) em vez de extraídas dinamicamente dos dados, o que pode causar erros se a ordem dos dados mudar.

### 3. Markdown cells são na verdade comentários de código
- Todas as "seções" do notebook usam `#` e `##` dentro de **code cells** ao invés de células Markdown, o que impede a renderização correta dos títulos.

---

## 🏗️ Problemas de Tecnologia e Formato

### 1. Dependência do Google Colab
- `from google.colab import files` + `files.upload()` **só funciona no Colab**
- Não é reproduzível localmente sem modificação
- O badge "Open in Colab" amarra o projeto a uma plataforma

### 2. Dados não versionados
- Os 4 arquivos Excel **não estão no repositório**
- Não há como reproduzir a análise sem os dados originais
- Sem documentação de fonte dos dados

### 3. Visualização limitada (apenas matplotlib)
- Gráficos estáticos, sem interatividade
- Impossível fazer zoom, hover com detalhes, ou filtrar dados
- Notebooks no GitHub renderizam matplotlib pobremente

### 4. Sem gerenciamento de dependências
- Nenhum `requirements.txt`, `pyproject.toml` ou `environment.yml`
- Impossível saber as versões exatas usadas

### 5. Sem `.gitignore`
- Falta ignorar `__pycache__/`, `.ipynb_checkpoints/`, `.DS_Store`, etc.

---

## 🧹 Problemas de Qualidade de Código

### 1. Duplicação massiva de código
O mesmo padrão de carregamento/limpeza de dados é repetido **4 vezes** (uma para cada arquivo Excel), com as mesmas operações:
```python
xlsx = pd.ExcelFile("arquivo.xlsx")
sheet_names = xlsx.sheet_names
df = pd.read_excel(xlsx, sheet_names[0])
df.columns = df.iloc[0].values.tolist()
df.drop([0,1,26,28,29,30,31,32], inplace=True)
# ... mesma sequência toda vez
```

### 2. Nomes de variáveis não descritivos
- `df`, `df2`, `df3`, `df4` → Não indicam o conteúdo
- `xlsx`, `xlsx2`, `xlsx3`, `xlsx4` → Mesma coisa
- `y1`, `y2`, `y3` → Sem contexto

### 3. Números mágicos
- `df.drop([0,1,26,28,29,30,31,32], inplace=True)` — por que esses índices? Nenhum comentário explica
- `df = df[:-7]` — remove as últimas 7 linhas sem explicação

### 4. Código comentado deixado no notebook
- Várias linhas comentadas (`#df.drop`, `#df.index`, etc.) que são resquícios de desenvolvimento

### 5. Sem funções, classes ou modularização
- Tudo em células soltas sem encapsulamento
- Zero reutilização de código

### 6. Configurações globais de matplotlib
- `plt.rcParams` alterados no topo sem reset, pode causar efeitos colaterais

---

## 🚀 Propostas de Melhoria

### Fase 1: Correções Imediatas ✅
- [x] Corrigir labels do eixo Y nos gráficos de empregados
- [x] Converter comentários `#` em células Markdown reais
- [x] Remover dependência do Google Colab
- [x] Remover código comentado
- [x] Adicionar `.gitignore`

### Fase 2: Modernização da Estrutura
- [x] Criar `requirements.txt` com dependências modernas
- [ ] Incluir arquivos de dados no repositório (`data/`)
- [ ] Criar módulo Python reutilizável (`src/`) com funções de carregamento e plotagem
- [ ] Adicionar README.md atualizado

### Fase 3: Modernização Tecnológica

#### 📊 Visualizações Interativas com Plotly
Substituir matplotlib por **Plotly Express** para:
- Gráficos interativos (hover, zoom, pan)
- Melhor renderização no GitHub e em qualquer browser
- Export como HTML standalone

#### 🗺️ Mapas Geográficos
- **Plotly Choropleth** ou **Folium/GeoPandas** para visualizar dados por estado em mapas do Brasil
- Mapas de calor por município de São Paulo

#### 📱 Dashboard Interativo (Streamlit ou Panel)
Criar um dashboard web com:
- Filtros dinâmicos (estado, período, métrica)
- Comparação lado-a-lado entre estados
- Possibilidade de deploy gratuito (Streamlit Cloud, Railway, etc.)

#### 📓 Migrar para Quarto ou Marimo
- **Quarto** (`.qmd`): Renderiza como site estático, PDF, ou apresentação — perfeito para trabalhos acadêmicos
- **Marimo** (`.py`): Notebooks reativos que funcionam como apps, sem os problemas do Jupyter

### Fase 4: Melhorias de Análise

#### 📈 Análises Estatísticas
- Calcular taxas de crescimento (CAGR) por estado/município
- Análise de tendência (regressão linear, média móvel)
- Identificar outliers e pontos de inflexão
- Correlação entre nº de estabelecimentos e nº de empregados

#### 🦠 Incluir Dados Pós-2019
- Atualizar com dados do período pandêmico (2020-2022) e pós-pandemia
- Fonte sugerida: **RAIS/CAGED** via [Base dos Dados](https://basedosdados.org/) ou portal do Governo
- Analisar impacto real da pandemia (que era o tema do TCC)

#### 🏭 Contextualização do Setor
- Adicionar anotações em eventos importantes (ex: pandemia, crise dos chips)
- Incluir dados de importação/exportação de semicondutores
- Comparar com tendências globais

### Fase 5: DevOps e Qualidade

- [ ] Configurar CI/CD com GitHub Actions para validar o notebook
- [ ] Adicionar testes unitários para funções de ETL
- [ ] Configurar linting (ruff/black) para código Python
- [ ] Adicionar pre-commit hooks
- [ ] Containerizar com Docker para reprodutibilidade total

---

## 🛠️ Stack Tecnológica Sugerida

| Componente | Atual | Proposto |
|---|---|---|
| Ambiente | Google Colab | Jupyter Lab / Marimo / Quarto |
| Visualização | matplotlib | **Plotly Express** + matplotlib |
| Mapas | — | **Plotly** / Folium / GeoPandas |
| Dashboard | — | **Streamlit** |
| Dados | Upload manual (.xlsx) | Arquivos versionados / API |
| Dependências | Nenhum | `pyproject.toml` + `uv` |
| Formatação | — | Ruff / Black |
| CI/CD | — | GitHub Actions |

---

## 📂 Estrutura de Diretórios Proposta

```
microeletronica/
├── data/
│   ├── raw/                    # Dados originais (xlsx)
│   └── processed/              # Dados limpos (csv/parquet)
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Funções de carregamento e limpeza
│   ├── visualizations.py       # Funções de visualização reutilizáveis
│   └── analysis.py             # Funções de análise estatística
├── notebooks/
│   └── analise_microeletronica.ipynb  # Notebook principal (limpo)
├── app/
│   └── dashboard.py            # Dashboard Streamlit
├── tests/
│   └── test_data_loader.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── README.md
└── MELHORIAS.md
```

---

## 🎯 Prioridade de Implementação

1. **Imediato**: Correções de bugs + remover dependência Colab *(esta branch)*
2. **Curto prazo**: Incluir dados, refatorar código, adicionar Plotly
3. **Médio prazo**: Dashboard Streamlit, mapas geográficos
4. **Longo prazo**: Atualizar dados, análises estatísticas avançadas, CI/CD
