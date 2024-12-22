import http.server
import json
import os
from urllib.parse import urlparse

TASKS_FILE = "tasks.txt"
tasks = []


def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    if tasks:
        return max(task["id"] for task in tasks) + 1
    return 1


def generate_id():
    if tasks:
        return max(task["id"] for task in tasks) + 1
    return 1

class TodoHandler(http.server.BaseHTTPRequestHandler):

    def _send_response(self, status, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/tasks":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(post_data)
                if "title" not in data or "priority" not in data:
                    self._send_response(400, {"error": "Missing required fields: title and priority."})
                    return

                new_task = {
                    "title": data["title"],
                    "priority": data["priority"],
                    "isDone": False,
                    "id": generate_id()
                }
                tasks.append(new_task)
                save_tasks()
                self._send_response(201, new_task)
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid JSON format."})

        elif parsed_path.path.startswith("/tasks/") and parsed_path.path.endswith("/complete"):
            try:
                task_id = int(parsed_path.path.split("/")[2])
                task = next((task for task in tasks if task["id"] == task_id), None)
                if not task:
                    self._send_response(404, {"error": "Task not found."})
                    return

                task["isDone"] = True
                save_tasks()
                self._send_response(200)
            except ValueError:
                self._send_response(400, {"error": "Invalid task ID."})

    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/tasks":
            self._send_response(200, tasks)
        else:
            self._send_response(404, {"error": "Not found."})


if __name__ == "__main__":
    load_tasks()
    server = http.server.HTTPServer(("", 8000), TodoHandler)
    print("Starting server at http://localhost:8000")
    server.serve_forever()
