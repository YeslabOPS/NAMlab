from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_config

def set_static_route(task: Task) -> Result:
    if task.host.platform == "cisco_xe":
        commands = [
            "ip route 192.168.100.0 255.255.255.0 192.168.0.1",
            "write"
        ]
    elif task.host.platform == "huawei_vrpv8":
        commands = [
            "ip route-static 192.168.100.0 24 192.168.0.1",
            "commit",
            "save",
            "y",
        ]
    else:
        return Result(
            host=task.host,
            result="Unsupported platform",
            failed=True
        )

    result = task.run(task=netmiko_send_config, config_commands=commands)
    return result

if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=set_static_route)

    for host, task_result in result.items():
        print(f"Host: {host} - Result: {task_result.result}")
