import requests

params = {"id": 202}

response = requests.post('http://192.168.86.210/svi_bodovi', params=params)

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)
