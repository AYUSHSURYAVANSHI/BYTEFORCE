from flask import Flask, jsonify, request
app = Flask(__name__)

# In a real-world scenario, you would use a database to store todos.
# For demonstration purposes, we'll use a list to store todos.
todos = []

# Routes
# Get all todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Add a new todo
@app.route('/api/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Update a todo
@app.route('/api/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    updated_todo = request.json
    todos[index] = updated_todo
    return jsonify(updated_todo)

# Delete a todo
@app.route('/api/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    del todos[index]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
