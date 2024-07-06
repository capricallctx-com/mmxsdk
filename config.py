# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024, Caprica LLC
import loguru
import requests
import context


def config_get(hsid: str):
    """
    Fetches the current configuration settings from the server.

    :param hsid: Session ID for authentication.
    :return: The current configuration settings as a JSON string, or None if the request fails.
    """
    url = f"{context.base_url}/wapi/config/get"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def config_set(hsid: str, key: str, value: str):
    """
    Updates a configuration setting on the server.

    :param hsid: Session ID for authentication.
    :param key: The configuration key to update.
    :param value: The new value for the configuration key.
    :return: The response from the server as a JSON string, or None if the request fails.
    """
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
