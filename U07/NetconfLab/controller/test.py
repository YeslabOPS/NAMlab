import requests
from cisco import Cisco

url = 'http://127.0.0.1:5000/api/cisco/loopback'
def test_main():
    payload = {'ifname': '110',
               'ifip': '100.100.101.1'}

    resp = requests.post(url, json=payload)
    print(resp.text)

def test_cisco():
    tester = Cisco()
    result = tester.manage_if('100', '100.100.100.106', '255.255.255.0', 'merge')
    print(result)

test_main()