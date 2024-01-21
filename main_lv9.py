#ZADATAK 4

# from flask import Flask, request, make_response

# app = Flask("Predavanje")

# @app.post('/temperatura')
# def post_temperatura():
#     response = make_response()
#     print(request.data)
#     response.data = 'Uspješno ste postavili temperaturu'
#     response.status_code = 201
#     return response

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=80)   


import requests

# ZADATAK 5
# response1 = requests.get('http://192.168.1.104')

# print(response1.text)
# print(response1.status_code)

# payload = {"ON": '31.9'}

# response2 = requests.post('http://192.168.1.104', json=payload)

# print(response2.text)
# print(response2.status_code)


#ZADATAK 6
response3 = requests.post('http://192.168.1.104', "ON")

print(response3.text)
print(response3.status_code)