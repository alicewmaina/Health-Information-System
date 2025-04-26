class HealthProgram:
    def __init__(self, name):
        self.name = name

class Client:
    def __init__(self, client_id, name, age):
        self.client_id = client_id
        self.name = name
        self.age = age
        self.enrolled_programs = [] 