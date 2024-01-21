import requests

response = requests.get('http://192.168.1.100')

payload = {"temperatura": 31.9}

response = requests.post('http://192.168.1.100', json=payload)

