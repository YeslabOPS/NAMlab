from ncclient import manager


class BaseController:
    def __init__(self, host, username, password):
        login_info = {"host": host,
                      "port": 830,
                      "username": username,
                      "password": password,
                      "hostkey_verify": False,
                      "device_params": {'name': 'huaweiyang'},
                      }

        self.inst = manager.connect(**login_info)

    def if_check(self, **kwargs):
        return None

    def if_update(self, **kwargs):
        return None

    def close(self):
        self.inst.close_session()