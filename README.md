# Health Information System

A professional Flask-based health information system that manages clients and health programs through a RESTful API.

# Here is a link to my powerpoint presentation

https://www.canva.com/design/DAGlvd39HLU/g_PHuj1vHM8W5Jmq0C7VJA/edit?utm_content=DAGlvd39HLU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Project Structure

```
/health_system
│
├── run.py              # Application entry point
├── requirements.txt    # Project dependencies
│
├── /app
│   ├── __init__.py    # Flask application factory
│   ├── routes.py      # API endpoints
│   ├── models.py      # Data models
│   └── storage.py     # In-memory storage
│
└── README.md
```

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python run.py
```

## API Endpoints

| Feature | Method | Endpoint | Request Body |
|---------|--------|----------|--------------|
| Create Program | POST | `/programs` | `{"name": "Program Name"}` |
| Register Client | POST | `/clients` | `{"client_id": "1", "name": "James bill", "age": 30}` |
| Enroll Client | PUT | `/clients/<client_id>/enroll` | `{"programs": ["Program Name"]}` |
| Search Clients | GET | `/clients/search?name=John` | - |
| View Client | GET | `/clients/<client_id>` | - |
| Delete Client | DELETE | `/clients/<client_id>` | - |

## Example Usage

### Create a Health Program
```bash
curl -X POST http://localhost:5000/programs \
  -H "Content-Type: application/json" \
  -d '{"name": "HIV Program"}'
```

### Register a Client
```bash
curl -X POST http://localhost:5000/clients \
  -H "Content-Type: application/json" \
  -d '{"client_id": "1", "name": "James bill", "age": 30}'
```

### Enroll a Client in Programs
```bash
curl -X PUT http://localhost:5000/clients/1/enroll \
  -H "Content-Type: application/json" \
  -d '{"programs": ["HIV Program"]}'
```

### Search for Clients
```bash
curl http://localhost:5000/clients/search?name=James
```

### View Client Profile
```bash
curl http://localhost:5000/clients/1
```

### Delete a Client
```bash
curl -X DELETE http://localhost:5000/clients/1
``` 