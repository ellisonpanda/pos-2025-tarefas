# users.py
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {
    1: {"id": 1, "nome": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "nome": "Bob", "email": "bob@example.com"}
}
next_id = 3

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        abort(404)
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    if not data or 'nome' not in data or 'email' not in data:
        abort(400)
    user = {"id": next_id, "nome": data['nome'], "email": data['email']}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        abort(404)
    data = request.get_json()
    user.update({k: data[k] for k in ['nome', 'email'] if k in data})
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
