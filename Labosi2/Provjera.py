from flask import Flask, request, redirect, url_for, make_response

app = Flask("Prva flask aplikacija")


@app.put('/putanja_put')
def prvi():
    return 'putanja_za_bod', 405


@app.get('/putanja_get')
def drugi():
    url = request.args.get('samo_jako')
    resp = make_response('hocu_bodove', url)
    return resp

@app.get('/jos_malo_pa_gotovo')
def treci():
    json = {'moji_bodovi': 3}
    resp = make_response(json, 201)
    return resp


@app.post('/hocu_sve_bodove')
def cetvrti():
    url = request.json.get('svi_bodovi')
    resp = make_response('svi_bodovi', url)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)