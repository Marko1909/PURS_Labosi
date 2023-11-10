import requests

payload = {"temperatura": '24.3'}

response = requests.post('http://192.168.86.216/temperatura', json=payload)

print(response.text)
print(response.status_code)
