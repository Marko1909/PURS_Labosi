import requests

response = requests.delete('http://192.168.86.216/temperatura', id=2)

print(response.text)
print(response.status_code)

#print(response.json().get('temperatura'))
