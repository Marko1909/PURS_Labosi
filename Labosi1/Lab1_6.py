import requests

params = {"id": 19}

response = requests.delete('http://192.168.86.210/temperatura', params=params)

print(response.text)
print(response.status_code)