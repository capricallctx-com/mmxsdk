# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024, Caprica LLC
import json
import loguru
import requests
import context
from context import headers

def node_info(hsid: str):
    """
    Fetches information about the node.

    :param hsid: Session ID for authentication.
    :return: Node information as a JSON string, or None if the request fails.
    """
    s = requests.Session()
    cookies = {'hsid': hsid}

    url = f"{context.base_url}/wapi/node/info"
    print(url)
    response = s.get(url, cookies=cookies, headers=context.headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None
    print(response.text)
    return response.text

def node_offers(hsid: str):
    """
    Retrieves the current offers made by the node.

    :param hsid: Session ID for authentication.
    :return: A JSON object containing the offers, or None if the request fails.
    """
    s = requests.Session()
    cookies = {'hsid': hsid}

    url = f"{context.base_url}/wapi/node/offers?limit=2000"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None

    return json.loads(response.text)

def node_exit(hsid: str):
    """
    Signals the node to exit or shutdown.

    :param hsid: Session ID for authentication.
    :return: A JSON object confirming the exit, or None if the request fails.
    """
    s = requests.Session()
    cookies = {'hsid': hsid}
    url = f"{context.base_url}/wapi/node/exit"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None

    return json.loads(response.text)

def node_log(hsid: str, limit=1000, level="INFO", module="all"):
    """
    Fetches the log entries of the node.

    :param hsid: Session ID for authentication.
    :param limit: The maximum number of log entries to retrieve.
    :param level: The log level to filter by (e.g., INFO, ERROR).
    :param module: The module to filter log entries by. Use "all" for no filtering.
    :return: A JSON object containing the log entries, or None if the request fails.
    """
    s = requests.Session()
    cookies = {'hsid': hsid}

    url = f"{context.base_url}/wapi/node/log?limit={limit}&level={level}&module={module}"
    print(url)
    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None

    return json.loads(response.text)

def node_graph_blocks(hsid: str, limit=100, step=1):
    """
    Retrieves a graph of blocks from the node.

    :param hsid: Session ID for authentication.
    :param limit: The maximum number of blocks to include in the graph.
    :param step: The step size to use when fetching blocks.
    :return: A JSON object containing the graph blocks, or None if the request fails.
    """
    s = requests.Session()
    cookies = {'hsid': hsid}
    url = f"/node/graph/blocks?limit={limit}&step={step}"

    response = s.get(url, cookies=cookies, headers=headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return json.loads(response.text)