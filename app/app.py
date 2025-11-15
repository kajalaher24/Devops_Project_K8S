from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    app_env = os.getenv("APP_ENV", "development")
    app_version = os.getenv("APP_VERSION", "v1")
    return f"Welcome to DevOps Project with Kubernetes!<br>Environment: {app_env}<br>Version: {app_version}"
    return f"Welcome to CICD Pipelines"

@app.route('/about')
def about():
    db_password = os.getenv("DB_PASSWORD", "not_set")
    return f"This is a Flask app deployed on Kubernetes.<br>DB Password: {db_password}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

