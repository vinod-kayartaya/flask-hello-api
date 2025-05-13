from flask import Flask
import os

app = Flask("hello-api")


@app.get("/api/hello/<string:name>")
def index(name):
    return f"Hello, {name}"

@app.get("/api/hello")
def index2():
    return f"Hello, friend"

port = os.environ.get("APP_PORT", 5200)
app.run(host="0.0.0.0", port=port)