import json

GET_SESSION = {'__type': 'vnx.addons.HttpSession', 'hsid': '', 'login_time': 0, 'permissions': ['mmx.permission_e.PUBLIC', 'vnx.addons.permission_e.FILE_DOWNLOAD', 'vnx.addons.permission_e.HTTP_REQUEST'], 'session_timeout': 0, 'user': '', 'vsid': 3172659233693079713}


class MMXSession:
    def __init__(self, json_str=None):
        self.__type = 'vnx.addons.HttpSession'
        self.hsid = ''
        self.login_time = 0
        self.permissions = ['mmx.permission_e.PUBLIC', 'vnx.addons.permission_e.FILE_DOWNLOAD', 'vnx.addons.permission_e.HTTP_REQUEST']
        self.session_timeout = 0
        self.user = ''
        self.vsid = 0

        if json_str:
            self.__dict__ = json.loads(json_str)

    def to_json(self):
        return json.dumps(self.__dict__)