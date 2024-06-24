import json
import loguru
import requests
import context


def get_balances(hsid: str, index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/balance?index={index}&show_all=true"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None
    return response.text


def get_token_list(hsid: str, index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/coins?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def mint(hsid: str, index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/mint?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None
    return response.text


def send(hsid: str, token_id: str, amount: float, destination: str, index: int = context.default_wallet, memo: str = ""):
    url = f"{context.base_url}/wapi/wallet/send"
    payload = {
        "index": index,
        "amount": amount,
        "currency": token_id,
        "dst_addr": destination,
        "options": {
            "memo": memo,
            "fee_ratio": 1024,
            "passphrase": None
        }
    }
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.post(url, cookies=cookies, headers=context.headers, json=payload)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def deploy(hsid: str, contract_json: str, index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/deploy?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    print(contract_json)
    response = s.post(url, cookies=cookies, headers=context.headers, data=contract_json)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def offer(hsid: str, ask_token_id: str, ask_amount: float, selling_token_id: str, selling_amount: float,
          index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/offer"
    payload = {
        "index": index,
        "bid": selling_amount,
        "ask": ask_amount,
        "bid_currency": selling_token_id,
        "ask_currency": ask_token_id
    }

    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.post(url, cookies=cookies, headers=context.headers, json=payload)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
    return response.text


def cancel_offer(hsid: str, token_id: str, options: str,
          index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/cancel_offer"
    payload = {
        "index": index,
        "address": token_id,
        "options": options
    }

    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.post(url, cookies=cookies, headers=context.headers, json=payload)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
    return response.text

def accept_offer(hsid: str, offer_id: str, options: str,
          index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/accept_offer"
    payload = {
        "index": index,
        "address": offer_id,
        "options": options
    }

    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.post(url, cookies=cookies, headers=context.headers, json=payload)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
    return response.text
