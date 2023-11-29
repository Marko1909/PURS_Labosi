from flask import Flask, request, session, redirect, url_for, make_response, render_template
import jinja2

app = Flask("Prva flask aplikacija")

lista = [
    'Prvi tekstualni element',
    'Drugi tekstualni element',
    'Treci tekstualni element',
    'Cetvrti tekstualni element'
]

@app.get('/')
def provjera():
    response = render_template('provjera5.html', naslov='Provjera', test='Testif poruka', liste=lista)
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)