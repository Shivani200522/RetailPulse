import json
from pathlib import Path


class BusinessRules:

    def __init__(self):
        config_dir = Path(__file__).resolve().parents[2] / "config"

        with open(config_dir / "seasonality.json", "r") as f:
            self.seasonality = json.load(f)

        with open(config_dir / "payment_rules.json", "r") as f:
            self.payment_rules = json.load(f)

        with open(config_dir / "simulation_rules.json", "r") as f:
            self.simulation_rules = json.load(f)

    def get_month_weights(self, month: int):
        return self.seasonality["months"].get(str(month), {})

    def get_weekend_multiplier(self):
        return self.seasonality["weekend_multiplier"]

    def get_salary_multiplier(self):
        return self.seasonality["salary_day_multiplier"]

    def get_payment_methods(self):
        return self.payment_rules["payment_methods"]

    def get_payment_success_rate(self):
        return self.payment_rules["payment_success_rate"]

    def get_simulation_rules(self):
        return self.simulation_rules