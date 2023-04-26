from flask import Flask

app  = Flask(__name__)

@app.route("/hello")
def hello():
    print("Incoming request for /hello")
    return "Hello World! \n"

if __name__ == "__main__":
    app.run(port=8024)