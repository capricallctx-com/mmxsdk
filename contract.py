# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024, Caprica LLC
import json
import loguru
import requests
import context


def exec_history(hsid: str, id: str, limit: int):
    """
    Fetches the execution history of a specific contract.

    This function retrieves the execution history of a contract identified by its ID, limited to a specified number of recent executions. The history includes various execution details such as transaction IDs, execution results, and timestamps.

    :param hsid: Session ID for authentication.
    :param id: The ID of the contract to fetch the execution history for.
    :param limit: The maximum number of execution records to retrieve.
    :return: A JSON object containing the execution history of the contract, or logs an error if the request fails.
    """
    url = f"{context.base_url}/wapi/contract/exec_history?id={id}&limit={limit}"
    s = requests.Session()
    cookies = {'hsid': hsid}
    response = s.get(url, cookies=cookies, headers=context.headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to GET {url}: {response.status_code}, {response.text}")
    return json.loads(response.text)





