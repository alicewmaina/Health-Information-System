from flask import request, jsonify
from app.storage import clients, programs, save_clients, save_programs

def register_routes(app):
    # Helper function for error responses
    def error_response(message, status_code=400):
        return jsonify({"error": message}), status_code

    # Create a health program
    @app.route("/programs", methods=["POST"])
    def create_program():
        data = request.json
        program_name = data.get("name")
        if not program_name:
            return error_response("Program name is required")

        # Check for duplicate program
        if any(program["name"] == program_name for program in programs):
            return error_response("Program already exists")

        program = {"id": len(programs) + 1, "name": program_name}
        programs.append(program)
        save_programs()
        return jsonify(program), 201

    # Register a new client
    @app.route("/clients", methods=["POST"])
    def register_client():
        data = request.json
        client_id = data.get("client_id")
        name = data.get("name")
        age = data.get("age")

        if not client_id or not name or not age:
            return error_response("Client ID, name, and age are required")

        # Check for duplicate client ID
        if any(client["client_id"] == client_id for client in clients):
            return error_response("Client ID already exists")

        client = {"client_id": client_id, "name": name, "age": age, "programs": []}
        clients.append(client)
        save_clients()
        return jsonify(client), 201

    # Enroll a client in programs
    @app.route("/clients/<client_id>/enroll", methods=["PUT"])
    def enroll_client(client_id):
        data = request.json
        program_names = data.get("programs")

        if not program_names:
            return error_response("Program names are required")

        # Find the client
        client = next((c for c in clients if c["client_id"] == client_id), None)
        if not client:
            return error_response("Client not found", 404)

        # Enroll the client in programs
        for program_name in program_names:
            if not any(p["name"] == program_name for p in programs):
                return error_response(f"Program '{program_name}' does not exist")
            if program_name not in client["programs"]:
                client["programs"].append(program_name)

        save_clients()
        return jsonify(client), 200

    # Search for clients by name
    @app.route("/clients/search", methods=["GET"])
    def search_clients():
        name = request.args.get("name", "").lower()
        matching_clients = [c for c in clients if name in c["name"].lower()]
        return jsonify(matching_clients), 200

    # View a client's profile
    @app.route("/clients/<client_id>", methods=["GET"])
    def view_client(client_id):
        client = next((c for c in clients if c["client_id"] == client_id), None)
        if not client:
            return error_response("Client not found", 404)
        return jsonify(client), 200

    # Delete a client
    @app.route("/clients/<client_id>", methods=["DELETE"])
    def delete_client(client_id):
        client = next((c for c in clients if c["client_id"] == client_id), None)
        if not client:
            return error_response("Client not found", 404)

        clients.remove(client)
        save_clients()
        return jsonify({"message": "Client deleted"}), 200