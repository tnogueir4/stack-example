from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World 003!"

@app.route("/version")
def vers():
    return "App v3.0"

@app.route("/server")
def serv():
    return "container 03"

if __name__ == '__main__':
  app.run(debug=True)