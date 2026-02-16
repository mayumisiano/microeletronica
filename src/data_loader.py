from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

FILES = {
    "estab_estados": "estabelecimentos_estados.xlsx",
    "estab_municipios_sp": "estabelecimentos_municipios_sp.xlsx",
    "empreg_estados": "empregados_estados.xlsx",
    "empreg_municipios_sp": "empregados_municipios_sp.xlsx",
}

DATASETS_META: dict[str, dict] = {
    "estab_estados": {
        "row_label": "UF",
        "drop_total": True,
        "title": "Estabelecimentos por Estado",
        "ylabel": "Nº de Estabelecimentos",
        "description": (
            "Quantidade de estabelecimentos do setor de microeletrônica por unidade federativa."
        ),
    },
    "estab_municipios_sp": {
        "row_label": "Município-São Paulo",
        "drop_total": False,
        "title": "Estabelecimentos por Município (SP)",
        "ylabel": "Nº de Estabelecimentos",
        "description": "Quantidade de estabelecimentos nos municípios paulistas.",
    },
    "empreg_estados": {
        "row_label": "UF",
        "drop_total": True,
        "title": "Empregados por Estado",
        "ylabel": "Nº de Empregados",
        "description": (
            "Quantidade de empregados no setor de microeletrônica por unidade federativa."
        ),
    },
    "empreg_municipios_sp": {
        "row_label": "Município-São Paulo",
        "drop_total": False,
        "title": "Empregados por Município (SP)",
        "ylabel": "Nº de Empregados",
        "description": "Quantidade de empregados nos municípios paulistas.",
    },
}


def load_excel(
    filepath: str | Path,
    row_label: str = "UF",
    drop_total: bool = True,
) -> pd.DataFrame:
    """Load and clean a RAIS Excel file, returning a transposed DataFrame (years x localities)."""
    path = Path(filepath)
    if not path.is_absolute():
        path = DATA_DIR / path

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}\nPlace .xlsx files in: {DATA_DIR}")

    xlsx = pd.ExcelFile(path)
    df = pd.read_excel(xlsx, xlsx.sheet_names[0])

    df.columns = df.iloc[0].values.tolist()

    drop_indices = [i for i in [0, 1, 26, 28, 29, 30, 31, 32] if i < len(df)]
    df = df.drop(drop_indices).reset_index(drop=True)

    df = df.dropna(how="all")

    df = df.T
    df.columns = df.iloc[0].values.tolist()
    df = df.drop(row_label)
    df = df.sort_index(ascending=True)

    if drop_total and "Total" in df.columns:
        df = df.drop("Total", axis=1)

    df = df.apply(pd.to_numeric, errors="coerce")
    df.index = df.index.astype(int).astype(str)

    return df


@dataclass
class Dataset:
    name: str
    df: pd.DataFrame
    title: str
    ylabel: str
    description: str

    @property
    def localities(self) -> list[str]:
        return list(self.df.columns)

    @property
    def years(self) -> list[str]:
        return list(self.df.index)

    @property
    def period(self) -> str:
        return f"{self.years[0]}-{self.years[-1]}"

    # backward-compat aliases (notebook)
    @property
    def nome(self) -> str:
        return self.name

    @property
    def titulo(self) -> str:
        return self.title

    @property
    def descricao(self) -> str:
        return self.description

    @property
    def localidades(self) -> list[str]:
        return self.localities

    @property
    def anos(self) -> list[str]:
        return self.years

    @property
    def periodo(self) -> str:
        return self.period


def load_dataset(name: str) -> Dataset:
    """Load a single dataset by key name, with metadata attached."""
    if name not in FILES:
        raise ValueError(f"Dataset '{name}' not found. Options: {list(FILES.keys())}")

    meta = DATASETS_META[name]
    df = load_excel(
        FILES[name],
        row_label=meta["row_label"],
        drop_total=meta["drop_total"],
    )

    return Dataset(
        name=name,
        df=df,
        title=meta["title"],
        ylabel=meta["ylabel"],
        description=meta["description"],
    )


def load_all() -> dict[str, Dataset]:
    """Load all available datasets, silently skipping missing files."""
    datasets = {}
    for name in FILES:
        try:
            datasets[name] = load_dataset(name)
        except FileNotFoundError:
            continue
    return datasets


def check_data() -> dict[str, bool]:
    """Check which data files are present on disk."""
    return {name: (DATA_DIR / filename).exists() for name, filename in FILES.items()}


# backward-compat aliases (notebook)
carregar_dataset = load_dataset
carregar_todos = load_all
verificar_dados = check_data
