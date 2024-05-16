from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('data.json') as f:
    data=json.load(f)
#Get data
@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data['user'])

#Method == POST, Create data
@app.route('/append', methods=['POST'])
def append_data():
    new_data = request.json
    if new_data and all(field in new_data for field in ["id", "name", "email", "age"]):
        data['user'].append(new_data)
        with open('data.json', 'w') as file: 
            json.dump(data, file, indent=4)  # indent=4 for pretty formatting
        return jsonify({'message': 'Data appended successfully'}), 200
    else:
        return jsonify({'error': 'No data provided'}), 400
    
#Method == PUT , Update data
@app.route('/append/<int:user_id>', methods=['PUT'])
def update_data(user_id):
    updated_data = request.json
    if updated_data and all(field in updated_data for field in ["name", "email", "age"]):
        for user in data['user']:
            if user['id'] == user_id:
                user.update(updated_data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
                return jsonify({'message': 'Data updated successfully'}), 200
        return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Invalid data provided'}), 400
    
#Method == DELETE, Delete the data
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_data(user_id):
    for user in data['user']:
        if user['id'] == user_id:
            data['user'].remove(user)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            return jsonify({'message': 'Data deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)