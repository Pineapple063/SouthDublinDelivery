from flask import Flask, render_template
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

@app.route("/")
def hello():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0')