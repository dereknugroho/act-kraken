import base64
import hashlib
import hmac
import os
import requests
import time
import urllib.parse

def get_kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

# Attaches auth headers and returns results of a POST request
def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req

if __name__ == '__main__':
    api_url = "https://api.kraken.com"
    api_key = os.environ['API_KEY_KRAKEN']
    api_sec = os.environ['API_SEC_KRAKEN']

    # REST: Account Balance
    # resp = kraken_request('/0/private/Balance', {
    #     "nonce": str(int(1000*time.time()))
    # }, api_key, api_sec)

    # REST: Ledger
    # resp = kraken_request('/0/private/Ledgers', {
    #     "nonce": str(int(1000*time.time())),
    # }, api_key, api_sec)

    # REST: Trade History
    # resp = kraken_request('/0/private/TradesHistory', {
    #     "nonce": str(int(1000*time.time()))
    # }, api_key, api_sec)

    # REST: Open Orders
    # resp = kraken_request('/0/private/OpenOrders', {
    #     "nonce": str(int(1000*time.time())),
    #     "trades": True
    # }, api_key, api_sec)

    # REST: Closed Orders
    # resp = kraken_request('/0/private/ClosedOrders', {
    #     "nonce": str(int(1000*time.time())),
    # }, api_key, api_sec)

    # REST: Add Order
    # resp = kraken_request('/0/private/AddOrder', {
    #     "nonce": str(int(1000*time.time())),
    #     "ordertype": "limit",
    #     "type": "sell",
    #     "volume": 0.0001205,
    #     "pair": "XBTCAD",
    #     "price": 
    # }, api_key, api_sec)

    # Order book for XBTCAD pair
    # resp = requests.get('https://api.kraken.com/0/public/Depth?pair=XBTCAD')

    print(resp.json())
