from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World 002!"

@app.route("/version")
def vers():
    return "App v2.0"

@app.route("/server")
def serv():
    return "container 02"

if __name__ == '__main__':
  app.run(debug=True)