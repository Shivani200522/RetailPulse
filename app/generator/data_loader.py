from pathlib import Path

import pandas as pd


class MasterDataLoader:
    """
    Loads all master datasets required by the RetailPulse simulator.
    """

    def __init__(self) -> None:
        base_dir = Path(__file__).resolve().parents[2]

        data_dir = base_dir / "data" / "sample"

        self.customers = pd.read_csv(data_dir / "customers.csv")

        self.products = pd.read_csv(data_dir / "products.csv")

        self.stores = pd.read_csv(data_dir / "stores.csv")