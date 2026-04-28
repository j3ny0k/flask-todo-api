from flask import Flask, jsonify, request, json

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


@app.route("/")
def home():
    return "Flask is working"


@app.route("/api/tasks")
def get_tasks():
    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title required"}), 400

    new_task = {"id": len(tasks) + 1, "title": data["title"], "done": False}

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


if __name__ == "__main__":
    app.run(debug=True)
