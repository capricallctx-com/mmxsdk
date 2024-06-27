import json

import loguru
import requests

import context


def header(hsid: str, block_hash=None, height=None):
    if block_hash is None and height is None:
        raise ValueError("block_hash or height must be provided")
    if block_hash is None:
        url = f"{context.base_url}/wapi/header?height={height}"
    else:
        url = f"{context.base_url}/wapi/header?hash={block_hash}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def block(hsid: str, block_hash=None, height=None):
    if block_hash is None and height is None:
        raise ValueError("block_hash or height must be provided")
    if block_hash is None:
        url = f"{context.base_url}/wapi/block?height={height}"
    else:
        url = f"{context.base_url}/wapi/block?hash={block_hash}"

    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def headers(hsid: str, offset, limit=200):
    url = f"{context.base_url}/wapi/headers?offset={offset}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def blocks(hsid: str, offset, limit=200):
    url = f"{context.base_url}/wapi/blocks?offset={offset}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def transaction(hsid: str, id=None):
    if id is None:
        raise ValueError("id must be provided")
    url = f"{context.base_url}/wapi/transaction?id={id}"

    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def transactions(hsid: str, height, offset, limit=200):
    url = f"{context.base_url}/wapi/transactions?height={height}&offset={offset}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def farmer(hsid: str, farmer_id: str, since_unix: int = 0, limit=200):
    url = f"{context.base_url}/wapi/farmer?id={farmer_id}&since={since_unix}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)

def farmers(hsid: str, since_unix: int = 0, limit=200):
    url = f"{context.base_url}/wapi/farmers?since={since_unix}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)

def address(hsid: str, id: str):
    url = f"{context.base_url}/wapi/address?id={id}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)

def balance(hsid: str, id: str):
    url = f"{context.base_url}/wapi/balance?id={id}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def contract(hsid: str, id: str):
    url = f"{context.base_url}/wapi/contract?id={id}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)

