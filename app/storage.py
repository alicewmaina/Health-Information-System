# programs = []
# # clients = {} 
import json
import os

# File paths for storing data
CLIENTS_FILE = "clients.json"
PROGRAMS_FILE = "programs.json"

# Helper function to load data from a file
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

# Helper function to save data to a file
def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Load clients and programs from files
clients = load_data(CLIENTS_FILE)
programs = load_data(PROGRAMS_FILE)

# Save clients and programs back to files
def save_clients():
    save_data(CLIENTS_FILE, clients)

def save_programs():
    save_data(PROGRAMS_FILE, programs)