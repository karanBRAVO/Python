from flask import Flask, render_template
import socket

app = Flask(__name__)
IP = socket.gethostbyname(socket.gethostname())
PORT = 12345

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/auth")
def authentication():
    return render_template("authentication.html")

@app.route("/chooseAvatar")
def chsImg():
    return render_template("chsImg.html")

if __name__ == "__main__":
    app.run(IP, PORT, debug=True)
