import loguru
import requests

import context


def config_get(hsid: str):
    url = f"{context.base_url}/wapi/config/get"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def config_set(hsid: str, key: str, value: str):
    url = f"{context.base_url}/wapi/config/set"
    payload = {
        "key": key,
        "value": value
    }
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.post(url, cookies=cookies, headers=context.headers, json=payload)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
    return response.text