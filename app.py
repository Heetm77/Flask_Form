from flask import Flask, render_template

# created app instance using the Flask class
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.run(debug=True, port=5001)