from flask import Flask

app = Flask("hello-api")


@app.get("/api/hello/<string:name>")
def index(name):
    return f"Hello, {name}"

@app.get("/api/hello")
def index2():
    return f"Hello, friend"

app.run(host="0.0.0.0", port=5200)