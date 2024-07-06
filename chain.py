# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024, Caprica LLC
import json
import loguru
import requests
import context


def header(hsid: str, block_hash=None, height=None):
    """
    Fetches the header of a block by its hash or height.

    :param hsid: Session ID for authentication.
    :param block_hash: The hash of the block to fetch. Optional if height is provided.
    :param height: The height of the block to fetch. Optional if block_hash is provided.
    :return: A JSON object containing the block header information.
    :raises ValueError: If neither block_hash nor height is provided.
    """
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
    """
    Fetches a full block by its hash or height.

    :param hsid: Session ID for authentication.
    :param block_hash: The hash of the block to fetch. Optional if height is provided.
    :param height: The height of the block to fetch. Optional if block_hash is provided.
    :return: A JSON object containing the full block information.
    :raises ValueError: If neither block_hash nor height is provided.
    """
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
    """
    Fetches a range of block headers.

    :param hsid: Session ID for authentication.
    :param offset: The starting point for fetching headers.
    :param limit: The maximum number of headers to fetch. Defaults to 200.
    :return: A JSON object containing a list of block headers.
    """
    url = f"{context.base_url}/wapi/headers?offset={offset}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def blocks(hsid: str, offset, limit=200):
    """
    Fetches a range of full blocks.

    :param hsid: Session ID for authentication.
    :param offset: The starting point for fetching blocks.
    :param limit: The maximum number of blocks to fetch. Defaults to 200.
    :return: A JSON object containing a list of full blocks.
    """
    url = f"{context.base_url}/wapi/blocks?offset={offset}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def transaction(hsid: str, id=None):
    """
    Fetches a transaction by its ID.

    :param hsid: Session ID for authentication.
    :param id: The ID of the transaction to fetch.
    :return: A JSON object containing the transaction information.
    :raises ValueError: If id is not provided.
    """
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
    """
    Fetches transactions for a specific block height.

    :param hsid: Session ID for authentication.
    :param height: The height of the block whose transactions are to be fetched.
    :param offset: The starting point for fetching transactions.
    :param limit: The maximum number of transactions to fetch. Defaults to 200.
    :return: A JSON object containing a list of transactions.
    """
    url = f"{context.base_url}/wapi/transactions?height={height}&offset={offset}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def farmer(hsid: str, farmer_id: str, since_unix: int = 0, limit=200):
    """
    Fetches information about a specific farmer.

    :param hsid: Session ID for authentication.
    :param farmer_id: The ID of the farmer to fetch information for.
    :param since_unix: The starting Unix timestamp for fetching farmer activities. Defaults to 0.
    :param limit: The maximum number of records to fetch. Defaults to 200.
    :return: A JSON object containing information about the farmer.
    """
    url = f"{context.base_url}/wapi/farmer?id={farmer_id}&since={since_unix}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def farmers(hsid: str, since_unix: int = 0, limit=200):
    """
    Fetches information about multiple farmers.

    :param hsid: Session ID for authentication.
    :param since_unix: The starting Unix timestamp for fetching farmer activities. Defaults to 0.
    :param limit: The maximum number of records to fetch. Defaults to 200.
    :return: A JSON object containing information about multiple farmers.
    """
    url = f"{context.base_url}/wapi/farmers?since={since_unix}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def address(hsid: str, id: str):
    """
    Fetches information about a specific address.

    :param hsid: Session ID for authentication.
    :param id: The ID of the address to fetch information for.
    :return: A JSON object containing information about the address.
    """
    url = f"{context.base_url}/wapi/address?id={id}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def balance(hsid: str, id: str):
    """
    Fetches the balance for a specific address.

    :param hsid: Session ID for authentication.
    :param id: The ID of the address to fetch the balance for.
    :return: A JSON object containing the balance information for the address.
    """
    url = f"{context.base_url}/wapi/balance?id={id}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)


def contract(hsid: str, id: str):
    """
    Fetches information about a specific contract.

    :param hsid: Session ID for authentication.
    :param id: The ID of the contract to fetch information for.
    :return: A JSON object containing information about the contract.
    """
    url = f"{context.base_url}/wapi/contract?id={id}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)
