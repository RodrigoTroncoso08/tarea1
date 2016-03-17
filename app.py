import os
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/validarFirma', methods=['POST'])
def validar():
    valid = False
    message = request.form['mensaje']
    hashU = request.form['hash']

    m = hashlib.sha256()
    m.update(message)
    hashr = m.hexdigest
    if hashr==hashU:
        valid=True

    return jsonify( {'mensaje': message}, {'valido' : valid})

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
