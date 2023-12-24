from flask import Flask, request, session, redirect, url_for, make_response, render_template, g
import jinja2
import MySQLdb


app = Flask("Prva flask aplikacija")


app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.before_request
def before_request_func():
    g.connection = MySQLdb.connect(host="localhost", user="app", passwd="1234", db="lvj6")
    g.cursor = g.connection.cursor()

    if request.path.startswith('/static'):
        return #Skip the login check for static files
    if request.path == '/login' or request.path == '/static' or request.path == '/temperatura':
        return
    if session.get('username') is None:
        return redirect(url_for('login'))
    

@app.after_request
def after_request_func(response):
    g.connection.commit()
    g.connection.close()
    return response


@app.get('/')
def index():
    id = request.args.get('id')
    if id == None or id == '1':
        g.cursor.execute(render_template('getKorTemp.sql', id_korisnika=session.get('id')))
        list_temp = g.cursor.fetchall()

        response = render_template('index.html', naslov='Početna stranica', username=session.get('username').capitalize(), tip='Temperatura', podatci=list_temp)
        return response, 200
    
    elif id == '2':
        g.cursor.execute(render_template('getKorVlage.sql', id_korisnika=session.get('id')))
        list_vlage = g.cursor.fetchall()

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
    g.cursor.execute(render_template('selectKorisnik.sql', user=request.form.get('username'), pasw=request.form.get('password')))
    korisnik = g.cursor.fetchall()

    if korisnik != ():
        session['username'] = korisnik[0][3]
        session['id'] = korisnik[0][0]
        return redirect(url_for('index'))
    else:
        return render_template('login.html', naslov='Stranica za prijavu', poruka='Uneseni su pogrešni podatci!')


@app.post('/temperatura')
def put_temperatura():
    global temperatura
    response = make_response()

    if request.json.get('temperatura') is not None:
        query = render_template('writeTemperature.sql', value=request.json.get('temperatura'))
        g.cursor.execute(query)
        response.data = 'Uspješno ste postavili temperaturu'
        response.status_code = 201
    else:
        response.data = 'Niste napisali ispravan ključ'
        response.status_code = 404
    return response


@app.route('/temperatura/<int:id_podatka>', methods=['POST'])
def delete(id_podatka):
    if id_podatka is not None:
        query = render_template('deleteTemp.sql', id_temp=id_podatka)
        g.cursor.execute(query)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)