from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ACCOUNTS_FILE = 'accounts.json'

def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'w') as f:
            json.dump([], f)
    with open(ACCOUNTS_FILE, 'r') as f:
        return json.load(f)

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f, indent=2)

@app.route('/accounts', methods=['GET'])
def get_accounts():
    return jsonify(load_accounts())

@app.route('/accounts', methods=['POST'])
def add_account():
    data = request.get_json()
    accounts = load_accounts()
    accounts.append(data)
    save_accounts(accounts)
    return jsonify({'message': 'Account added'})

@app.route('/switch/<int:index>', methods=['GET'])
def switch_account(index):
    accounts = load_accounts()
    if 0 <= index < len(accounts):
        return jsonify({'message': 'Switched', 'account': accounts[index]})
    return jsonify({'error': 'Invalid account index'}), 404

if __name__ == '__main__':
    app.run(debug=True)
