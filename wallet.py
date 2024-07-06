# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024, Caprica LLC
import io
import loguru
import requests
import context


def get_balances(hsid: str, index: int = context.default_wallet) -> str:
    """
    Fetches the balance information for a specified wallet.

    :param hsid: Session ID for authentication.
    :param index: Index of the wallet to query.
    :return: JSON string with balance information or None if the request fails.
    """
    url = f"{context.base_url}/wapi/wallet/balance?index={index}&show_all=true"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None
    return response.text


def get_token_list(hsid: str, index: int = context.default_wallet) -> str:
    """
    Retrieves a list of tokens available in the specified wallet.

    :param hsid: Session ID for authentication.
    :param index: Index of the wallet to query.
    :return: JSON string with a list of tokens or None if the request fails.
    """
    url = f"{context.base_url}/wapi/wallet/coins?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def mint(hsid: str, index: int = context.default_wallet) -> str:
    """
    Mints new tokens in the specified wallet.

    :param hsid: Session ID for authentication.
    :param index: Index of the wallet for minting tokens.
    :return: JSON string with minting result or None if the request fails.
    """
    url = f"{context.base_url}/wapi/wallet/mint?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get /wapi/node/info: {response.status_code}, {response.text}")
        return None
    return response.text


def send(hsid: str, token_id: str, amount: float, destination: str, index: int = context.default_wallet,
         memo: str = "") -> str:
    """
    Sends a specified amount of tokens to a destination address.

    :param hsid: Session ID for authentication.
    :param token_id: ID of the token to send.
    :param amount: Amount of tokens to send.
    :param destination: Destination address.
    :param index: Index of the sender's wallet.
    :param memo: Optional memo for the transaction.
    :return: JSON string with transaction result or None if the request fails.
    """
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


def deploy(hsid: str, contract_json: str, index: int = context.default_wallet) -> str:
    """
    Deploys a contract to the blockchain.

    :param hsid: Session ID for authentication.
    :param contract_json: JSON string representing the contract to deploy.
    :param index: Index of the wallet deploying the contract.
    :return: JSON string with deployment result or None if the request fails.
    """
    url = f"{context.base_url}/wapi/wallet/deploy?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    print(contract_json)
    contract_file = io.StringIO(contract_json)
    response = s.post(url, cookies=cookies, headers=context.headers, data=contract_file)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to POST {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def offer(hsid: str, ask_token_id: str, ask_amount: float, selling_token_id: str, selling_amount: float,
          index: int = context.default_wallet) -> str:
    """
    Creates a trade offer on the blockchain.

    :param hsid: Session ID for authentication.
    :param ask_token_id: ID of the token being asked for.
    :param ask_amount: Amount of tokens being asked for.
    :param selling_token_id: ID of the token being sold.
    :param selling_amount: Amount of tokens being sold.
    :param index: Index of the wallet making the offer.
    :return: JSON string with offer result or None if the request fails.
    """
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


def cancel_offer(hsid: str, token_id: str, options: str, index: int = context.default_wallet) -> str:
    """
    Cancels an existing trade offer.

    :param hsid: Session ID for authentication.
    :param token_id: ID of the token related to the offer to cancel.
    :param options: Additional options for the cancellation.
    :param index: Index of the wallet cancelling the offer.
    :return: JSON string with cancellation result or None if the request fails.
    """
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


def accept_offer(hsid: str, offer_id: str, options: str, index: int = context.default_wallet) -> str:
    """
    Accepts an existing trade offer.

    :param hsid: Session ID for authentication.
    :param offer_id: ID of the offer to accept.
    :param options: Additional options for accepting the offer.
    :param index: Index of the wallet accepting the offer.
    :return: JSON string with acceptance result or None if the request fails.
    """
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


def keys(hsid: str, index: int = context.default_wallet) -> str:
    """
    Retrieves the public and private keys of the specified wallet.

    :param hsid: Session ID for authentication.
    :param index: Index of the wallet to retrieve keys for.
    :return: JSON string with keys information or None if the request fails.
    """
    url = f"{context.base_url}/wapi/wallet/keys?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return response.text


def seed(hsid: str, index: int = context.default_wallet) -> str:
    """
    Fetches the seed phrase of the specified wallet.

    :param hsid: Session ID for authentication.
    :param index: Index of the wallet to retrieve the seed for.
    :return: Seed phrase string or None if the request fails.
    """
    url = f"{context.base_url}/wapi/wallet/seed?index={index}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get {url}: {response.status_code}, {response.text}")
        return None
    return response.text
