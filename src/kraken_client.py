import json

from src.config import config, get_kraken_keys
from src.kraken_auth import request

def make_request(path: str, body: dict = None):
    """A wrapper for making API requests."""
    public_key, private_key = get_kraken_keys()
    response = request(
        method=config["method"],
        path=path,
        body=body,
        public_key=public_key,
        private_key=private_key,
        environment=config["environment"]
    )

    return json.loads(response.read().decode("utf-8"))
