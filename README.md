# Flask Todo API

Simple backend API for managing tasks.

## Features

- Get all tasks
- Get one task by id
- Create new task
- Update task (done)
- Delete task
- JSON file storage (tasks.json)

---

## Endpoints

### GET /

Check if server is running.

Response:

```json
{
  "message": "Flask is working"
}
```

---

### GET /api/tasks

Get all tasks.

Response:

```json
[
  {
    "id": 1,
    "title": "test",
    "done": false
  }
]
```

---

### GET /api/tasks/1

Get one task by id.

Response:

```json
{
  "id": 1,
  "title": "learn flask",
  "done": false
}
```

If task not found:

```json
{
  "error": "task not found"
}
```

---

### POST /api/tasks

Create a new task.

Request:

```json
{
  "title": "learn flask"
}
```

Response:

```json
{
  "id": 1,
  "title": "learn flask",
  "done": false
}
```

---

### PATCH /api/tasks/1

Update task (mark as done/undone).

Request:

```json
{
  "done": true
}
```

Response:

```json
{
  "id": 1,
  "title": "learn flask",
  "done": true
}
```

---

### DELETE /api/tasks/1

Delete a task.

Response:

```json
{
  "message": "task deleted"
}
```

---

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start server:

```bash
python app.py
```

Server:

```
http://127.0.0.1:5000
```

---

## Notes

- Data is stored in `tasks.json`
- `tasks.json` is ignored by git
- IDs are generated automatically
