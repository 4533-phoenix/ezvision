import werkzeug.exceptions
import network_vision
import flask_socketio
import logging
import psutil
import utils
import flask
import time
import os

# logging.basicConfig(level=logging.DEBUG)

SERVER_PATH = os.path.dirname(os.path.realpath(__file__))
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("PORT", 8080)
NAME = "EZ Vision"

os.chdir(SERVER_PATH)
app = flask.Flask(__name__)
socket = flask_socketio.SocketIO(app, cors_allowed_origins="*")

# vision1 = network_vision.ColoredBallsVision("", "frontCamera")

@app.errorhandler(werkzeug.exceptions.HTTPException)
def page_not_found(error):
    with open("./client/templates/error.thtml", "r") as file:
        data = file.read()

    return data.replace(
        "{status}", str(error.code)
        ).replace(
            "{message}", "".join(error.description)
        ).replace(
            "{name}", NAME
        ), error.code

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def send_file(path):
    path = os.path.abspath(os.path.join("./client/dist", path.replace("../", "")))

    if os.path.isdir(path):
        index_path = os.path.join(path, "index.html")

        if os.path.isfile(index_path):
            path = index_path

    if not os.path.exists(path) or os.path.isdir(path):
        flask.abort(404)

    return flask.send_file(path)

@socket.on("command")
def handle_command(data):
    os.system(data)

@socket.on("resources")
def handle_resources():
    flask_socketio.emit("resources", {
        "CPU %": psutil.cpu_percent(),
        "Used RAM %": psutil.virtual_memory().percent,
        "Availible RAM %": round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1),
        **utils.net_usage()
    })

if __name__ == "__main__":
    print(f"Server running on http://localhost:{PORT}/")
    socket.run(app, host=HOST, port=PORT)