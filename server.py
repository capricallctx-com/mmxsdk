# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Caprica LLC
import os

import requests
import context
import loguru
from schema import MMXSession

"""
# uncomment this to enable debugging of the HTTP requests
import logging

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
"""


def login(username='mmx-admin', password=os.getenv("PASSWORD")):
    """
    generate a new session for the user based on a local account
    default username is mmx_admin
    default password is PASSWORD from the environment
    :param username:
    :param password:
    :return: None on error or access denied, a Session object on success
    """
    s = requests.Session()
    cookies = {'hsid': None}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla', }
    url = f"{context.base_url}/server/login?user={username}&passwd_plain={password}"
    response = s.get(url, cookies=cookies, headers=headers)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to login: {response.status_code}, {response.text}")
        return None
    return MMXSession(response.text)


def get_session():
    """
    get the current session for the user
    :return:
    """
    url = f"{context.base_url}/server/session"
    response = requests.get(url)
    if response.status_code != 200:
        loguru.logger.error(f"Failed to get session: {response.status_code}, {response.text}")
        return None
    my_session = MMXSession(response.text)
    if my_session.hsid == '' or my_session.hsid is None:
        loguru.logger.error("No session ID returned - you aren't logged in yet")
        return None
    return my_session
