import requests
requests.packages.urllib3.disable_warnings()

login_info = {"host": "192.168.0.221",
              "username": "restconf",
              "password": "restconf123"}


def check_ospf_config():
    # OSPF配置查看函数
    ospf_api = "/restconf/data/Cisco-IOS-XE-native:native/router"
    ospf_uri = "https://" + login_info["host"] + ospf_api
    headers = {'Content-Type': 'application/yang-data+json','Accept': 'application/yang-data+json'}

    ospf_check_result = requests.get(url=ospf_uri,
                                     auth=(login_info["username"],login_info["password"]),
                                     headers=headers,
                                     verify=False)
    #print(ospf_check_result.text)
    return ospf_check_result


def del_ospf():
    # OSPF配置删除函数
    ospf_api = "/restconf/data/Cisco-IOS-XE-native:native/router"
    ospf_uri = "https://" + login_info["host"] + ospf_api
    headers = {'Content-Type': 'application/yang-data+json','Accept': 'application/yang-data+json'}

    ospf_del_result = requests.delete( url=ospf_uri,
                                       auth=(login_info["username"],login_info["password"]),
                                       headers=headers,
                                       verify=False)
    if ospf_del_result.ok:
        print("OSPF配置已清空")
    else:
        print("删除失败，目前仍保留的OSPF配置如下：")
        print(check_ospf_config().text)


def modify_ospf(data):
    # OSPF配置新增函数
    ospf_api = "/restconf/data/Cisco-IOS-XE-native:native/router"
    ospf_uri = "https://" + login_info["host"] + ospf_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    ospf_config_result = requests.put(url=ospf_uri,
                                      auth=(login_info["username"], login_info["password"]),
                                      data=data,
                                      headers=headers,
                                      verify=False)

    if ospf_config_result.ok:
        print("配置完成，配置数据如下：")
        print(check_ospf_config().text)
    else:
        print("配置失败，原因如下：")
        print(ospf_config_result.reason)


def loop_if_add(data):
    # 环回口添加函数
    loop_api = "/restconf/data/Cisco-IOS-XE-native:native/interface"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_add_result = requests.post(url=loop_uri,
                                   auth=(login_info["username"], login_info["password"]),
                                   data=data,
                                   headers=headers,
                                   verify=False)

    if loop_add_result.ok:
        print("配置完成，配置数据如下：")
        print(loop_if_check().text)
    else:
        print("配置失败，原因如下：")
        print(loop_add_result.reason)


def loop_if_check():
    # 环回口查看
    loop_api = "/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_check_result = requests.get(url=loop_uri,
                                     auth=(login_info["username"], login_info["password"]),
                                     headers=headers,
                                     verify=False)
    #print(loop_check_result.text)
    return loop_check_result


def loop_ospf(data):
    # OSPF应用到环回接口
    loop_api = "/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_ospf_result = requests.put(url=loop_uri,
                                    auth=(login_info["username"], login_info["password"]),
                                    data=data,
                                    headers=headers,
                                    verify=False)

    if loop_ospf_result.ok:
        print("配置完成，配置数据如下：")
        print(loop_if_check().text)
    else:
        print("配置失败，原因如下：")
        print(loop_ospf_result.reason)


def loop_del(if_num):
    # 删除环回接口
    loop_api = f"/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback={if_num}"
    loop_uri = "https://" + login_info["host"] + loop_api
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

    loop_del_result = requests.delete(url=loop_uri,
                                      auth=(login_info["username"], login_info["password"]),
                                      headers=headers,
                                      verify=False)

    if loop_del_result.ok:
        print("环回接口已删除，目前环回接口配置如下：")
        loop_if_check()
    else:
        print("删除失败，目前环回接口配置如下：")
        loop_if_check()