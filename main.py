from flask import Flask, render_template, jsonify, send_file
import hashlib
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/hash/<string:cadena>')
def hashnojson(cadena):
    h256 = hashlib.sha256(cadena.encode()).hexdigest()
    h384 = hashlib.sha384(cadena.encode()).hexdigest()
    h224 = hashlib.sha224(cadena.encode()).hexdigest()
    h512 = hashlib.sha512(cadena.encode()).hexdigest()
    h1 = hashlib.sha1(cadena.encode()).hexdigest()
    list = [h256,h384,h224,h512,h1]

    return render_template('template.html', cadenas=list)

@app.route('/hash/<string:cadena>/json')
def hasjson(cadena):
    h256 = hashlib.sha256(cadena.encode()).hexdigest()
    h384 = hashlib.sha384(cadena.encode()).hexdigest()
    h224 = hashlib.sha224(cadena.encode()).hexdigest()
    h512 = hashlib.sha512(cadena.encode()).hexdigest()
    h1 = hashlib.sha1(cadena.encode()).hexdigest()

    return jsonify(h256=h256,h384=h384,h224=h224,h512=h512,h1=h1)

if __name__ == '__main__':
    app.run(debug=True)
