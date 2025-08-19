# Crypto Auto Trader on Kraken (CAT-Kraken)

Crypto Auto Trader on Kraken (CAT-Kraken) is an automated cryptocurrency trading app that executes trades on the [Kraken platform](https://www.kraken.com/).

CAT will execute a trade in a specific cryptocurrency if the result will be a net profit of 1 basis point. This is achieved through the usage of limit orders.

The trading criteria is based on:

- Price of your latest complete BTC/USD trade
- 30-day trade volume (for fee calculation)

## Setup

1. Obtain an API key from [Kraken](https://pro.kraken.com/).

2. Save your public API key as an environment variable called `API_KEY_KRAKEN`:
```
echo 'API_KEY_KRAKEN=your_public_kraken_api_key' >> .env
```

3. Save your private API key as an environment variable called `API_SEC_KRAKEN`:
```
echo 'API_SEC_KRAKEN=your_private_kraken_api_key' >> .env
```

4. Manually purchase any amount of BTC/USD using the Kraken web interface.

5. Clone this repository:
```
git clone https://github.com/dereknugroho/cat-kraken.git
cd cat-kraken
```

## Usage

Execute `main.py`:

```
python3 main.py
```

## Important

In order to maximize profitability, `main.py` must be executed at regular intervals for an extended period of time. This task is left up to you.

This app makes up to 5 API calls per execution. Kraken API usage limits are described [here](https://support.kraken.com/articles/360045239571-trading-rate-limits).

## Disclaimer

This is not a paid product. By using any snippets or derivative ideas from this repository, you personally accept any and all risks associated with trading cryptocurrency.

Furthermore, you agree not to pursue legal action against the owner of this repository for any consequences related to the usage of any part of the source code herein.
