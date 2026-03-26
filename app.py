from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Study Python", "completed": False},
    {"id": 2, "title": "Practice APIs", "completed": True},
]

def find_task(task_id: int):
    return next((task for task in tasks if task["id"] == task_id), None)

@app.get("/tasks")
def get_tasks():
    return jsonify(tasks)

@app.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    new_task = {
        "id": max((task["id"] for task in tasks), default=0) + 1,
        "title": title,
        "completed": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.patch("/tasks/<int:task_id>")
def update_task(task_id: int):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(silent=True) or {}
    if "completed" in data:
        task["completed"] = bool(data["completed"])
    if "title" in data and data["title"]:
        task["title"] = data["title"]
    return jsonify(task)

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
