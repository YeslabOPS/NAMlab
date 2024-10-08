import requests
requests.packages.urllib3.disable_warnings()

login_info = {"host": "你的设备IP",
              "username": "你的restconf用户",
              "password": "你的restconf密码"}


def check_ospf_config():
    # OSPF配置查看函数
    ospf_api = "/restconf/data/Cisco-IOS-XE-native:native/router"
    ospf_uri = "https://" + login_info["host"] + ospf_api
    headers = {'Content-Type': 'application/yang-data+json','Accept': 'application/yang-data+json'}

    ospf_check_result = requests.request("GET",
                                         url=ospf_uri,
                                         auth=(login_info["username"],login_info["password"]),
                                         headers=headers,
                                         verify=False)
    print(ospf_check_result.text)


def del_ospf():
    # OSPF配置删除函数
    ospf_api = "/restconf/data/Cisco-IOS-XE-native:native/router"
    ospf_uri = "https://" + login_info["host"] + ospf_api
    headers = {'Content-Type': 'application/yang-data+json','Accept': 'application/yang-data+json'}

    ospf_del_result = requests.request("DELETE",
                                       url=ospf_uri,
                                       auth=(login_info["username"],login_info["password"]),
                                       headers=headers,
                                       verify=False)
    if ospf_del_result.ok:
        print("OSPF配置已清空")
    else:
        print("删除失败，目前仍保留的OSPF配置如下：")
        check_ospf_config()


def modify_ospf(data):
    # OSPF配置新增函数
    ospf_api = "/restconf/data/Cisco-IOS-XE-native:native/router"
    ospf_uri = "https://" + login_info["host"] + ospf_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    ospf_config_result = requests.request("PUT",
                                          url=ospf_uri,
                                          auth=(login_info["username"], login_info["password"]),
                                          data=data,
                                          headers=headers,
                                          verify=False)

    if ospf_config_result.ok:
        print("配置完成，配置数据如下：")
        check_ospf_config()
    else:
        print("配置失败，原因如下：")
        print(ospf_config_result.reason)


def loop_if_add(data):
    # 环回口添加函数
    loop_api = "/restconf/data/Cisco-IOS-XE-native:native/interface"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_add_result = requests.request("POST",
                                       url=loop_uri,
                                       auth=(login_info["username"], login_info["password"]),
                                       data=data,
                                       headers=headers,
                                       verify=False)

    if loop_add_result.ok:
        print("配置完成，配置数据如下：")
        loop_if_check()
    else:
        print("配置失败，原因如下：")
        print(loop_add_result.reason)


def loop_if_check():
    # 环回口查看
    loop_api = "/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_check_result = requests.request("GET",
                                         url=loop_uri,
                                         auth=(login_info["username"], login_info["password"]),
                                         headers=headers,
                                         verify=False)
    print(loop_check_result.text)


def loop_ospf(data):
    # OSPF应用到环回接口
    loop_api = "/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_ospf_result = requests.request("PUT",
                                        url=loop_uri,
                                        auth=(login_info["username"], login_info["password"]),
                                        data=data,
                                        headers=headers,
                                        verify=False)

    if loop_ospf_result.ok:
        print("配置完成，配置数据如下：")
        loop_if_check()
    else:
        print("配置失败，原因如下：")
        print(loop_ospf_result.reason)


def loop_del(if_num):
    # 删除环回接口
    loop_api = f"/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback={if_num}"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_del_result = requests.request("DELETE",
                                       url=loop_uri,
                                       auth=(login_info["username"], login_info["password"]),
                                       headers=headers,
                                       verify=False)

    if loop_del_result.ok:
        print("环回接口已删除，目前环回接口配置如下：")
        loop_if_check()
    else:
        print("删除失败，目前环回接口配置如下：")
        loop_if_check()