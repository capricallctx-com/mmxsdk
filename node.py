import json

import loguru
import requests

import context


def node_info(hsid: str):
    s = requests.Session()
    cookies = {'hsid': hsid}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}

    url = f"{context.base_url}/wapi/node/info"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None
    print(response.text)
    return response.text

def node_offers(hsid: str):
    s = requests.Session()
    cookies = {'hsid': hsid}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}

    url = f"{context.base_url}/wapi/node/offers?limit=2000"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None

    return json.loads(response.text)

def node_exit(hsid: str):
    s = requests.Session()
    cookies = {'hsid': hsid}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}

    url = f"{context.base_url}/wapi/node/exit"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None

    return json.loads(response.text)

def node_log(hsid: str, limit = 1000, level = "INFO", module = "all"):
    s = requests.Session()
    cookies = {'hsid': hsid}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}

    url = f"{context.base_url}/wapi/node/log?limit={limit}&level={level}&module={module}"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None

    return json.loads(response.text)

def node_graph_blocks(hsid: str, limit = 100, step = 1):
    s = requests.Session()
    cookies = {'hsid': hsid}
    url = f"/node/graph/blocks?limit={limit}&step={step}"
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}
    response = s.get(url, cookies=cookies, headers=headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return json.loads(response.text)