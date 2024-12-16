from netmiko import ConnectHandler

def cisco_send(cmd, ip, username, password):
    device = {
        "device_type": "cisco_xe",
        "ip": ip,
        "port": 22,
        "username": username,
        "password": password,
    }
    conn = ConnectHandler(**device)
    data = conn.send_command(cmd)
    conn.disconnect()
    return data

def cisco_config(cmd_list, ip, username, password):
    device = {
        "device_type": "cisco_xe",
        "ip": ip,
        "port": 22,
        "username": username,
        "password": password,
    }
    conn = ConnectHandler(**device)
    conn.send_config_set(cmd_list)
    conn.disconnect()

class Record:
    def __init__(self):
        self.history = {"monitor_history":{},
                        "automation_history":{}}