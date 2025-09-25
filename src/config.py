import json
import os

from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config.json"

with open(CONFIG_PATH) as f:
    config = json.load(f)

def get_kraken_keys():
    """Safely attempt to retrieve Kraken API keys."""
    try:
        return os.environ["API_KEY_KRAKEN"], os.environ["API_SEC_KRAKEN"]
    except KeyError:
        raise RuntimeError("Kraken API keys not set in environment.")
