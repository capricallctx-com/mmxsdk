import requests
import context
import loguru
import logging
from schema import MMXSession
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


def login(username='mmx-admin', password=''):
    """
    generate a new session for the user based on a local account
    default username is mmx_admin
    default password is ''
    :param username:
    :param password:
    :return: None on error or access denied, a Session object on success
    """
    s = requests.Session()
    cookies = {'hsid': None}
    headers = {'Host': 'localhost:11380', 'User-Agent': 'Leozilla',}

    url = f"{context.base_url}/server/login?user={username}&passwd_plain={password}"
    print(url)

    response = s.get(url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        loguru.logger.error(f"Failed to login: {response.status_code}, {response.text}")
        return None
    return MMXSession(response.text)

"""
    GET /server/login?user=mmx_admin&passwd_plain=85341BD4A38868A9D8E1E93BFDDED7111C62F9FC63517A4B54D082B066CF3057 HTTP/1.1\r\n
    User-Agent: Leozilla\r\n
    Accept-Encoding: gzip, deflate\r\n
    Accept: */*\r\n
    Connection: keep-alive\r\n
    Host: localhost:11380\r\n
    Cookie: hsid\r\n
    \r\n
    [Full request URI: http://localhost:11380/server/login?user=mmx_admin&passwd_plain=85341BD4A38868A9D8E1E93BFDDED7111C62F9FC63517A4B54D082B066CF3057]
    [HTTP request 1/1]
    [Response in frame: 1382]

    GET /server/login?user=mmx-admin&passwd_plain=85341BD4A38868A9D8E1E93BFDDED7111C62F9FC63517A4B54D082B066CF3057 HTTP/1.1\r\n
    Host: localhost:11380\r\n
    Connection: keep-alive\r\n
    Pragma: no-cache\r\n
    Cache-Control: no-cache\r\n
    sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"\r\n
    sec-ch-ua-mobile: ?1\r\n
    User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36\r\n
    sec-ch-ua-platform: "Android"\r\n
    Accept: */*\r\n
    Sec-Fetch-Site: same-origin\r\n
    Sec-Fetch-Mode: cors\r\n
    Sec-Fetch-Dest: empty\r\n
    Referer: http://localhost:11380/gui/\r\n
    Accept-Encoding: gzip, deflate, br, zstd\r\n
    Accept-Language: en-US,en-XA;q=0.9,en;q=0.8\r\n
    Cookie: hsid=null\r\n
    \r\n
    [Full request URI: http://localhost:11380/server/login?user=mmx-admin&passwd_plain=85341BD4A38868A9D8E1E93BFDDED7111C62F9FC63517A4B54D082B066CF3057]
    [HTTP request 1/2]
    [Response in frame: 82]
    [Next request in frame: 84]


            /server/login?user=mmx-admin&passwd_plain=85341BD4A38868A9D8E1E93BFDDED7111C62F9FC63517A4B54D082B066CF3057
"""

def get_session():
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
