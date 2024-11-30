import requests

url = f'http://127.0.0.1:5000//dna/intent/api/v2/template-programmer/template/deploy'

data = {'mainTemplateId': '001',
        'forcePushTemplate': True,
        'isComposite': 'yes',
        'memberTemplateDeploymentInfo': [{'targetInfo': ['1.1.1.1', '2.2.2.2'],
                                          'hostName': 'YESLAB',
                                          'id': '123',
                                          'type': 'Switch',
                                          'versionedTemplateId': '1',
                                          'resourceParams': {'a':1},
                                          'params': {'b':1}
                                          }]}

response = requests.post(url, json=data)
print(response.json())