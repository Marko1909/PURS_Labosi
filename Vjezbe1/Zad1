import requests

response = requests.get('https://httpbin.org/user-agent')
for k, v in response.headers.items():
    print(f'{k}: {v}')

print()

print(response.json())