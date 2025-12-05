import pandas as pd
import requests
import yaml

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

def fetch_data():
    cfg = load_config()
    source_type = cfg["data"]["source_type"]

    if source_type == "csv":
        return pd.read_csv(cfg["data"]["csv_path"])

    elif source_type == "api":
        res = requests.get(cfg["data"]["api_url"])
        return pd.DataFrame(res.json())

    else:
        raise ValueError("Invalid source_type in config")