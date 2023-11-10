from flask import Flask, request, redirect, url_for, make_response

app = Flask("Prva flask aplikacija")

temp_list = []

@app.get('/')
def index():
    return 'Pocetna stranica'


@app.get('/login')
def login():
    return 'Stranica za prijavu'


@app.post('/login')
def provjera():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is not None and password is not None:
        if username == "PURS" and password == "1234":
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


@app.post('/temperatura')
def temperatura():
    temp = request.json.get('temperatura')

    if temp is not None:
        global temp_list
        temp_list.append(temp)
        return 'Uspješno ste postavili temperaturu', 201
    else:
        return 'Niste upisali ispravan ključ', 404


@app.get('/temperatura')
def zadnja_temp():
    global temp_list
    json = {'temperatura': temp_list[-1]}
    resp = make_response(json, 202)
    return resp


@app.delete('/temperatura')
def delete():
    global temp_list
    id = request.args.get('id')    
    
    if id is not None:
        temp_list.remove(int(id)-1)
        return 'Uspješno ste obrisali temperaturu', 202
    else:
        return 'upisali ste neispravan ključ', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)