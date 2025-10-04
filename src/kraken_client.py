import json

from config.config import config, get_kraken_keys
from src.kraken_auth import request

def make_request(path: str, body: dict = None):
    """A wrapper for making API requests."""
    public_key, private_key = get_kraken_keys()

    try:
        response = request(
            method=config["method"],
            path=path,
            body=body,
            public_key=public_key,
            private_key=private_key,
            environment=config["environment"]
        )
        data = json.loads(response.read().decode("utf-8"))

        # Handle Kraken's internal error response
        if data['error']:
            logger.error(f'Kraken API returned error(s): {data["error"]}')
            return None

        return data

    except Exception as e:
        logger.exception(f'Request to Kraken failed for path {path}: {e}')
        raise
