# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024, Caprica LLC
local_mmxnode = "http://localhost:11380"
public_rpc = "https://rpc.mmx.network"
base_url = local_mmxnode
headers = {'Host': 'localhost:11380', 'User-Agent': 'mmxsdk',} # dont think matters
default_wallet = 100

def set_base_url(url: str) -> str:
    """
    Sets the base URL for API requests.

    This function updates the global variable `base_url` with a new URL provided by the user.
    This URL is used as the base for making API requests throughout the application.

    :param url: The new base URL to be used for API requests.
    :return: The updated base URL.
    """
    global base_url
    base_url = url
    return base_url

def set_default_wallet(index: int) -> int:
    """
    Sets the default wallet index.

    This function updates the global variable `default_wallet` with a new index provided by the user.
    This index is used to identify the default wallet for transactions and queries when no specific wallet index is provided.

    :param index: The new default wallet index.
    :return: The updated default wallet index.
    """
    global default_wallet
    default_wallet = index
    return default_wallet
