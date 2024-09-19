# Crypto Auto Trader

Crypto Auto Trader (CAT) is an automated cryptocurrency trading app that executes trades on the [Kraken platform](https://www.kraken.com/).

CAT will execute a trade in a specified cryptocurrency that results in a net profit of 1 basis point. The trading criteria is based on the real-time bid-ask spread and the most recent trade of the same cryptocurrency.

## Setup

1. Obtain an API key on [Kraken Pro](https://pro.kraken.com/).

2. Save your public API key as an environment variable called `API_KEY_KRAKEN`:

`echo 'API_KEY_KRAKEN=your_public_api_key' >> .env`

3. Save your private API key as an environment variable called `API_SEC_KRAKEN`:

`echo 'API_SEC_KRAKEN=your_private_api_key' >> .env`

4. Manually purchase any cryptocurrency using the Kraken web interface.

5. Clone this repository:
```
git clone https://github.com/dereknugroho/cat-kraken.git
cd cat-kraken
```

## Usage

1. In `main.py`, set the value of `EXPECTED_TRADE_VOLUME` to a value less than or equal to the amount purchased in Step 4 of the Setup section.

2. Execute `main.py`:
```
python3 main.py
```

## Important

In order to maximize profitability, `main.py` must be executed at regular intervals for an extended period of time. This is task is left up to you.

Most users prefer to do this in the cloud, in which case you should run it as a Task in [PythonAnywhere](https://www.pythonanywhere.com/).

Note that this app makes 2 or 5 API calls **per execution**. If you spam it, your API key will become limited, as described [here](https://docs.kraken.com/api/docs/guides/spot-rest-ratelimits/).

## To-Do

:white_check_mark: Develop full test suite

:white_check_mark: Implement trade logging

:x: Utilize ML libraries to fit a [geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution) of short-term bid-ask spread movements

## Disclaimer

This is not a paid product.

By using any snippets or derivative ideas from this repository, you personally accept any and all risks associated with trading cryptocurrency.

Furthermore, you agree not to pursue any form of legal action against the owner of this repository.
