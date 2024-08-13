from ncclient import manager


class BaseController:
    def __init__(self, host, username, password, device_params=None):
        login_info = {"host": host,
                      "port": 830,
                      "username": username,
                      "password": password,
                      "hostkey_verify": False,
                      }
        if device_params:
            login_info["device_params"] = device_params

        self.inst = manager.connect(**login_info)

    def if_check(self, **kwargs):
        return None

    def if_update(self, **kwargs):
        return None

    def close(self):
        self.inst.close_session()