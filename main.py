from flask import Flask, request, session, redirect, url_for, make_response, render_template
import jinja2

app = Flask("Prva flask aplikacija")

list_temp = [
    {
        'datum': '29.09.2023',
        'vrijednost': 23
    },
    {
        'datum': '06.10.2023',
        'vrijednost': 21
    },
    {
        'datum': '13.10.2023',
        'vrijednost': 19
    },
    {
        'datum': '20.10.2023',
        'vrijednost': 25
    }
]

list_vlage = [
    {
        'datum': '29.09.2023',
        'vrijednost': 43
    },
    {
        'datum': '06.10.2023',
        'vrijednost': 59
    },
    {
        'datum': '13.10.2023',
        'vrijednost': 32
    },
    {
        'datum': '20.10.2023',
        'vrijednost': 21
    }
]

app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.before_request
def before_request_func():
    if request.path.startswith('/static'):
        return #Skip the login check for static files
    if request.path == '/login':
        return
    if session.get('username') is None:
        return redirect(url_for('login'))


@app.get('/')
def index():
    global list_vlage, list_temp
    id = request.args.get('id')
    if id == None or id == '1':
        response = render_template('index.html', naslov='Početna stranica', username=session.get('username').capitalize(), tip='Temperatura', podatci=list_temp)
        return response, 200
    elif id == '2':
        response = render_template('index.html', naslov='Početna stranica', username=session.get('username').capitalize(), tip='Vlaga', podatci=list_vlage)
        return response, 200


@app.get('/login')
def login():
    response = render_template('login.html', naslov='Stranica za prijavu')
    return response, 200


@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))


@app.post('/login')
def provjera():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'PURS' and password == '1234':
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return render_template('login.html', naslov='Stranica za prijavu', poruka='Uneseni su pogrešni podatci!')





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