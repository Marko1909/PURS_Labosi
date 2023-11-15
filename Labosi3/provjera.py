from flask import Flask, request, session, redirect, url_for, make_response, render_template

app = Flask("Prva flask aplikacija")


@app.get('/pocetna_stranica')
def login():
    response = render_template('provjera.html')
    return response

@app.post('/korisnicki_unos')
def provjera():
    text = request.form.get('text')
    password = request.form.get('password')
    email = request.form.get('email') 

    return f'{text}, {password}, {email}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)