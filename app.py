from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the User Management REST API!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({"error": "User not found"}), 404

# POST - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get("id")
    name = data.get("name")

    if not user_id or not name:
        return jsonify({"error": "Please provide both 'id' and 'name'"}), 400

    if user_id in users:
        return jsonify({"error": "User ID already exists"}), 409

    users[user_id] = {"name": name}
    return jsonify({"message": "User created", "user": users[user_id]}), 201

# PUT - Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Please provide a new name"}), 400

    users[user_id]['name'] = name
    return jsonify({"message": "User updated", "user": users[user_id]})

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user})

if __name__ == '__main__':
    app.run(debug=True)
