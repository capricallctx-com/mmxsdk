# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Caprica LLC
import json
import loguru
import requests
import context

"""
not that 'swap' in MMX is adding liquidity to a pool, not a token swap
those are offers - some functionality is currently not available for these
(at least i am not able to create a new liquidity pool)
"""

def list(hsid: str):
    """
    get a list of all the swap pools
    :param hsid:
    :return:
    """
    s = requests.Session()
    cookies = {'hsid': hsid}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}

    url = f"{context.base_url}/wapi/swap/list?limit=200&token=null&currency=null"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return json.loads(response.text)

def info(hsid: str, mmx_id: str):
    """
    get detailed information about a swap pool
    :param hsid:
    :param mmx_id:
    :return:
    """
    s = requests.Session()
    cookies = {'hsid': hsid}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}
    url = f"{context.base_url}/wapi/swap/info?id={mmx_id}"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    print(response.text)
    return response.text
