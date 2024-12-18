import os
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Abilita CORS

# Variabile per impostare la porta
SERVER_PORT = 4444  # Puoi cambiare questa porta come desideri

# Percorsi del certificato e della chiave
CERT_FILE = 'server.crt'
KEY_FILE = 'server.key'

# Generazione del certificato autofirmato se non esiste
if not (os.path.exists(CERT_FILE) and os.path.exists(KEY_FILE)):
    print("Certificato o chiave non trovati, generazione in corso...")
    subprocess.run([
        'openssl', 'req', '-x509', '-newkey', 'rsa:4096', '-sha256', '-nodes',
        '-keyout', KEY_FILE,
        '-out', CERT_FILE,
        '-days', '365',
        '-subj', '/C=XX/ST=State/L=City/O=Organization/OU=OrganizationUnit/CN=localhost'
    ], check=True)
    print("Certificato e chiave generati con successo.")

# Endpoint per ricevere i cookie
@app.route('/receive_cookies', methods=['POST'])
def receive_cookies():
    cookies = request.json.get('cookies', {})
    if cookies:
        print(f"Cookies ricevuti: {cookies}")
        return jsonify({"message": "Cookies ricevuti con successo"}), 200
    else:
        return jsonify({"message": "Nessun cookie fornito"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SERVER_PORT, ssl_context=(CERT_FILE, KEY_FILE))
