from flask import Flask
import pyodbc

app = Flask(__name__)

@app.route("/")
def index():
    return "Ciao Marco"

if __name__ == "__main__":
    app.run()