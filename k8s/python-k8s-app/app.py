from flask import Flask

app = Flask(__name__)

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "not found"

@app.route("/")
def hello():
    app_name = read_file("/config/APP_NAME")
    app_env = read_file("/config/APP_ENV")
    db_user = read_file("/secrets/DB_USER")

    return f"""
    App Name: {app_name}<br>
    Environment: {app_env}<br>
    DB User: {db_user}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

