## Author
Demetri Sanders  
Aspiring Software Engineer | Systems & Automation Background

# Simple REST API

A beginner-friendly REST API project built with Flask. This project manages a small in-memory task list and demonstrates basic API development concepts.

## Features
- Get all tasks
- Get one task by ID
- Create a new task
- Update task status
- Delete a task

## Tech Used
- Python
- Flask

## Project Structure
```text
simple-rest-api/
├── app.py
├── requirements.txt
├── test_app.py
└── README.md
```

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Endpoints
- `GET /tasks`
- `GET /tasks/<id>`
- `POST /tasks`
- `PATCH /tasks/<id>`
- `DELETE /tasks/<id>`

## Example POST Body
```json
{
  "title": "Finish homework"
}
```

## What I Practiced
- REST API basics
- JSON request/response handling
- CRUD operations
- Testing Flask endpoints
