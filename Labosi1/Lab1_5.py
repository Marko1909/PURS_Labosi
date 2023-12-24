import requests

payload = {"temperatura": '31.9'}

response = requests.post('http://192.168.1.100/temperatura', json=payload)

print(response.text)
print(response.status_code)
