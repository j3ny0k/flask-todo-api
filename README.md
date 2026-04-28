# Flask Todo API

Simple backend API for managing tasks.

## Features

- Get tasks
- Add new task
- Save tasks to JSON file

## Endpoints

### GET /api/tasks

Get all tasks.

Response:
[
{
"id": 1,
"title": "test",
"done": false
}
]

---

### POST /api/tasks

Create a new task.

Request:
{
"title": "learn flask"
}

Response:
{
"id": 1,
"title": "learn flask",
"done": false
}

---

## Run

python app.py

Server:
http://127.0.0.1:5000

---

## Notes

- Data is stored in tasks.json
- tasks.json is ignored by git
