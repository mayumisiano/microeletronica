"""
Módulo de ETL (Extract, Transform, Load) para dados da RAIS.

Responsável por carregar, limpar e transformar os dados brutos (.xlsx)
em DataFrames prontos para análise e visualização.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

# Arquivos esperados
ARQUIVOS = {
    "estab_estados": "Estabelecimentos_estados.xlsx",
    "estab_municipios_sp": "Analise_Estabelecimentos_3rank_municipio_sp.xlsx",
    "empreg_estados": "Analise_Funcionarios_3rank_estados.xlsx",
    "empreg_municipios_sp": "Analise_Funcionarios_3rank_municipio_sp.xlsx",
}

# Metadados de cada dataset
DATASETS_META: dict[str, dict] = {
    "estab_estados": {
        "label_linha": "UF",
        "remover_total": True,
        "titulo": "Estabelecimentos por Estado",
        "ylabel": "Nº de Estabelecimentos",
        "descricao": "Quantidade de estabelecimentos do setor de microeletrônica por unidade federativa.",
    },
    "estab_municipios_sp": {
        "label_linha": "Município-São Paulo",
        "remover_total": False,
        "titulo": "Estabelecimentos por Município de SP",
        "ylabel": "Nº de Estabelecimentos",
        "descricao": "Quantidade de estabelecimentos nos municípios paulistas.",
    },
    "empreg_estados": {
        "label_linha": "UF",
        "remover_total": True,
        "titulo": "Empregados por Estado",
        "ylabel": "Nº de Empregados",
        "descricao": "Quantidade de empregados no setor de microeletrônica por unidade federativa.",
    },
    "empreg_municipios_sp": {
        "label_linha": "Município-São Paulo",
        "remover_total": False,
        "titulo": "Empregados por Município de SP",
        "ylabel": "Nº de Empregados",
        "descricao": "Quantidade de empregados nos municípios paulistas.",
    },
}


# ---------------------------------------------------------------------------
# Funções de ETL
# ---------------------------------------------------------------------------


def carregar_excel(
    arquivo: str | Path,
    label_linha: str = "UF",
    remover_total: bool = True,
) -> pd.DataFrame:
    """
    Carrega e limpa um arquivo Excel de dados da RAIS.

    O formato esperado é:
    - Primeira linha real contém os nomes das colunas (localidades)
    - Linhas 0, 1, 26, 28-32 são cabeçalhos/rodapés a descartar
    - Dados precisam ser transpostos (localidades → colunas, anos → linhas)

    Parâmetros:
        arquivo: Caminho completo ou nome do arquivo dentro de DATA_DIR
        label_linha: Valor da primeira coluna a remover após transpor
        remover_total: Se True, remove a coluna 'Total'

    Retorna:
        DataFrame limpo: índice = anos (str), colunas = localidades, valores numéricos
    """
    caminho = Path(arquivo)
    if not caminho.is_absolute():
        caminho = DATA_DIR / caminho

    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho}\n"
            f"Coloque os arquivos .xlsx em: {DATA_DIR}"
        )

    xlsx = pd.ExcelFile(caminho)
    df = pd.read_excel(xlsx, xlsx.sheet_names[0])

    # Primeira linha contém os nomes reais das colunas
    df.columns = df.iloc[0].values.tolist()

    # Remove linhas de cabeçalho, totais e notas de rodapé
    indices_remover = [i for i in [0, 1, 26, 28, 29, 30, 31, 32] if i < len(df)]
    df = df.drop(indices_remover).reset_index(drop=True)

    # Remove linhas completamente vazias (rodapé)
    df = df.dropna(how="all")

    # Transpõe: localidades → colunas, anos → linhas
    df = df.T
    df.columns = df.iloc[0].values.tolist()
    df = df.drop(label_linha)
    df = df.sort_index(ascending=True)

    if remover_total and "Total" in df.columns:
        df = df.drop("Total", axis=1)

    # Converte tudo para numérico
    df = df.apply(pd.to_numeric, errors="coerce")

    return df


@dataclass
class Dataset:
    """Container para um dataset carregado com seus metadados."""

    nome: str
    df: pd.DataFrame
    titulo: str
    ylabel: str
    descricao: str

    @property
    def localidades(self) -> list[str]:
        return list(self.df.columns)

    @property
    def anos(self) -> list[str]:
        return list(self.df.index)

    @property
    def periodo(self) -> str:
        return f"{self.anos[0]}–{self.anos[-1]}"


def carregar_dataset(nome: str) -> Dataset:
    """
    Carrega um dataset pelo nome e retorna com metadados.

    Nomes válidos: 'estab_estados', 'estab_municipios_sp',
                   'empreg_estados', 'empreg_municipios_sp'
    """
    if nome not in ARQUIVOS:
        raise ValueError(
            f"Dataset '{nome}' não encontrado. "
            f"Opções: {list(ARQUIVOS.keys())}"
        )

    meta = DATASETS_META[nome]
    df = carregar_excel(
        ARQUIVOS[nome],
        label_linha=meta["label_linha"],
        remover_total=meta["remover_total"],
    )

    return Dataset(
        nome=nome,
        df=df,
        titulo=meta["titulo"],
        ylabel=meta["ylabel"],
        descricao=meta["descricao"],
    )


def carregar_todos() -> dict[str, Dataset]:
    """Carrega todos os datasets disponíveis. Ignora os que não encontrar."""
    datasets = {}
    for nome in ARQUIVOS:
        try:
            datasets[nome] = carregar_dataset(nome)
        except FileNotFoundError:
            continue
    return datasets


def verificar_dados() -> dict[str, bool]:
    """Verifica quais arquivos de dados estão disponíveis."""
    return {
        nome: (DATA_DIR / arquivo).exists()
        for nome, arquivo in ARQUIVOS.items()
    }
