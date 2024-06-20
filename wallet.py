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
    print(response.text)
    return response.text

def get_token_list(hsid: str, index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/coins?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    print(response.text)
    return response.text

def mint(hsid: str, index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/mint?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None
    print(response.text)
    return response.text


def send(hsid: str, token_id: str, amount: float, destination: str, index: int = context.default_wallet):
    url = f"{context.base_url}/wapi/wallet/send"
    payload = {
      "index": index,
      "amount": amount,
      "currency": token_id,
      "dst_addr": destination,
      "options": {
        "memo": "test test",
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
    print(response.text)
    return response.text