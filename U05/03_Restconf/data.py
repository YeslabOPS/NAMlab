old_ospf_data = '''
{
    "Cisco-IOS-XE-native:router": {
        "Cisco-IOS-XE-ospf:router-ospf": {
            "ospf": {
                "process-id": [
                    {
                        "id": 10
                    }
                ]
            }
        }
    }
}
'''

new_ospf_data = '''
{
    "Cisco-IOS-XE-native:router": {
        "Cisco-IOS-XE-ospf:router-ospf": {
            "ospf": {
                "process-id": [
                    {
                        "id": 1
                    },
                    {
                        "id": 2
                    },
                    {
                        "id": 3
                    },
                    {
                        "id": 4
                    },
                    {
                        "id": 5
                    }
                ]
            }
        }
    }
}
'''

loop_if_data = '''
{
    "Cisco-IOS-XE-native:Loopback": [
        {
            "name": 100,
            "ip": {
                "address": {
                    "primary": {
                        "address": "100.100.100.100",
                        "mask": "255.255.255.0"
                    }
                }
            }
        }
    ]
}
'''

loop_ospf_data = '''
{
    "Cisco-IOS-XE-native:Loopback": [
        {
            "name": 100,
            "ip": {
                "address": {
                    "primary": {
                        "address": "100.100.100.100",
                        "mask": "255.255.255.0"
                    }
                },
                "Cisco-IOS-XE-ospf:router-ospf": {
                    "ospf": {
                        "process-id": [
                            {
                                "id": 2,
                                "area": [
                                    {
                                        "area-id": 0
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }
    ]
}
'''