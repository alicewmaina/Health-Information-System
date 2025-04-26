from flask import Blueprint, request, jsonify
from app.models import Client, HealthProgram
from app import storage

main = Blueprint('main', __name__)

# Create a Health Program
@main.route('/programs', methods=['POST'])
def create_program():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Program name is required'}), 400

    program = HealthProgram(name)
    storage.programs.append(program)
    return jsonify({'message': f"Program '{name}' created successfully"}), 201

# Register a new Client
@main.route('/clients', methods=['POST'])
def register_client():
    data = request.json
    client_id = data.get('client_id')
    name = data.get('name')
    age = data.get('age')

    if not all([client_id, name, age]):
        return jsonify({'error': 'Client ID, Name and Age are required'}), 400

    if client_id in storage.clients:
        return jsonify({'error': 'Client ID already exists'}), 400

    client = Client(client_id, name, age)
    storage.clients[client_id] = client
    return jsonify({'message': f"Client '{name}' registered successfully"}), 201

# Enroll a client in programs
@main.route('/clients/<client_id>/enroll', methods=['PUT'])
def enroll_client(client_id):
    data = request.json
    program_names = data.get('programs', [])

    client = storage.clients.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    for pname in program_names:
        if pname not in [p.name for p in storage.programs]:
            return jsonify({'error': f"Program '{pname}' does not exist"}), 404
        if pname not in client.enrolled_programs:
            client.enrolled_programs.append(pname)

    return jsonify({'message': f"Client '{client.name}' enrolled successfully", 'programs': client.enrolled_programs}), 200

# Search for a client by name
@main.route('/clients/search', methods=['GET'])
def search_client():
    name_query = request.args.get('name', '')
    results = [vars(c) for c in storage.clients.values() if name_query.lower() in c.name.lower()]

    return jsonify({'results': results}), 200

# View client profile
@main.route('/clients/<client_id>', methods=['GET'])
def get_client_profile(client_id):
    client = storage.clients.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    return jsonify({
        'client_id': client.client_id,
        'name': client.name,
        'age': client.age,
        'enrolled_programs': client.enrolled_programs
    }), 200

# Delete a client
@main.route('/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = storage.clients.pop(client_id, None)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    return jsonify({'message': f"Client '{client.name}' deleted successfully"}), 200 