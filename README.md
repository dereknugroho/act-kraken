# Crypto Auto Trader on Kraken (CAT-Kraken)

Crypto Auto Trader on Kraken (CAT-Kraken) is an automated cryptocurrency trading app that executes trades on the [Kraken platform](https://www.kraken.com/).

CAT will execute a trade in a specific cryptocurrency if the result will be a net profit of 1 basis point.

The trading criteria is based on:

- The real-time bid-ask spread
- The most recent trade of the same cryptocurrency

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

4. Manually purchase any cryptocurrency using the Kraken web interface.

5. Clone this repository:
```
git clone https://github.com/dereknugroho/cat-kraken.git
cd cat-kraken
```

## Usage

1. In `main.py`, set the value of `EXPECTED_TRADE_VOLUME` to a non-negative value that is less than or equal to the amount manually purchased using the Kraken web interface in Step 4 of the **Setup** section.

2. Execute `main.py`:
```
python3 main.py
```

## Important

In order to maximize profitability, `main.py` must be executed at regular intervals for an extended period of time. This is task is left up to you.

If you wish to do this in the cloud, you should run the app as a collection of Tasks in [PythonAnywhere](https://www.pythonanywhere.com/).

Note that this app makes 2 to 5 API calls per execution. If you spam it, your API key will be subjected to the limits described [here](https://docs.kraken.com/api/docs/guides/spot-rest-ratelimits/).

## Disclaimer

This is not a paid product.

By using any snippets or derivative ideas from this repository, you personally accept any and all risks associated with trading cryptocurrency.
