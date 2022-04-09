import werkzeug.exceptions
import waitress
import flask
import os

SERVER_PATH = os.path.dirname(os.path.realpath(__file__))
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("PORT", 8080)
NAME = "EZ Vision"

os.chdir(SERVER_PATH)
app = flask.Flask(__name__)

@app.errorhandler(werkzeug.exceptions.HTTPException)
def page_not_found(error):
    with open("pages/error.thtml", "r") as file:
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
    path = os.path.abspath(os.path.join("client/dist", path.replace("../", "")))

    if os.path.isdir(path):
        index_path = os.path.join(path, "index.html")

        if os.path.isfile(index_path):
            path = index_path

    if not os.path.exists(path) or os.path.isdir(path):
        flask.abort(404)

    return flask.send_file(path)

@app.after_request
def apply_headers(response):
    response.headers["Server"] = "ezvision/1.0.0"
    return response

def get_app():
    return app

if __name__ == "__main__":
    print(f"Server running on http://localhost:{PORT}/")
    waitress.serve(app, host=HOST, port=PORT)
