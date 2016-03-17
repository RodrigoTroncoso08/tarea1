import os
from flask import Flask, request, jsonify, make_response
import hashlib
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/validarFirma', methods=['POST'])
def validar():
    valid = False
    message = request.form["mensaje"]
    hashU = request.form["hash"]

    message=  message.encode("utf-8")

    m = hashlib.sha256()
    m.update(message)
    hashr = m.hexdigest()

    if hashr==hashU.lower():
        valid=True

    return jsonify({'mensaje': message ,'valido' : valid})

@app.route('/status', methods=['GET'])
def stat():
	return  make_response(" ", 201)

@app.route('/texto', methods=['GET'])
def text():
    texto = urlopen("https://s3.amazonaws.com/files.principal/texto.txt").read()
    hText = texto.encode("utf-8")
    m = hashlib.sha256()
    m.update(hText)
    hashr = m.hexdigest()
    return jsonify({'mensaje': texto ,'hash' : hashr})

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
