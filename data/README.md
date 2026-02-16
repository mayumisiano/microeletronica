# Data

## Structure

```
data/
├── raw/                # Raw Excel files (RAIS)
│   ├── estabelecimentos_estados.xlsx
│   ├── estabelecimentos_municipios_sp.xlsx
│   ├── empregados_estados.xlsx
│   └── empregados_municipios_sp.xlsx
└── README.md
```

## Required files

Place the following Excel files in the `raw/` subfolder:

| File | Description |
|---|---|
| `estabelecimentos_estados.xlsx` | Microelectronics establishments by state (2006–2019) |
| `estabelecimentos_municipios_sp.xlsx` | Establishments in São Paulo municipalities |
| `empregados_estados.xlsx` | Employees by state |
| `empregados_municipios_sp.xlsx` | Employees in São Paulo municipalities |

## Data source

**RAIS** (Relação Anual de Informações Sociais) — Brazilian Ministry of Labor and Employment.

> Original data extracted from the [Brazilian Open Data Portal](http://dados.gov.br/) and filtered by the CNAE code for the microelectronics sector.
