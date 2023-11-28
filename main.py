from flask import Flask, request, session, redirect, url_for, make_response, render_template

app = Flask("Prva flask aplikacija")

temp_list = []

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
    response = render_template('index.html')
    return response, 200


@app.get('/login')
def login():
    response = render_template('login.html')
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