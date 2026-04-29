from flask import Flask, jsonify, request
import json

app = Flask(__name__)


def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


tasks = load_tasks()


@app.get("/")
def home():
    return jsonify({"message": "Flask is working"}), 200


@app.get("/api/tasks")
def get_tasks():
    return jsonify(tasks), 200


@app.get("/api/tasks/<int:task_id>")
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "task not found"}), 404
    
    return jsonify(task), 200


@app.post("/api/tasks")
def create_task():
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "title required"}), 400

    new_id = max((t["id"] for t in tasks), default=0) + 1

    new_task = {"id": new_id, "title": data["title"], "done": False}

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "task not found"}), 404

    tasks.remove(task)
    save_tasks(tasks)

    return jsonify({"message": "task deleted"}), 200


@app.patch("/api/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json()

    if not data or "done" not in data:
        return jsonify({"error": "done is required"}), 400

    if not isinstance(data["done"], bool):
        return jsonify({"error": "done must be boolean"}), 400

    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "task not found"}), 404

    task["done"] = data["done"]

    save_tasks(tasks)

    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True)
