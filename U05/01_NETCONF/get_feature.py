from ncclient import manager
from device import Device

# 通过 manager 建立 NETCONF 连接
with manager.connect(**Device) as cisco:
    print("连接成功!")
    capability_txt = ""
    # 通过连接实例的 server_capabilities 方法来获取设备的 NETCONF 能力特性
    for capability in cisco.server_capabilities:
        capability_txt += capability + "\n"
with open("iosxe_netconf_cap.txt", "w") as file:
    file.write(capability_txt)
print("设备能力已经写入到iosxe_netconf_cap.txt")

