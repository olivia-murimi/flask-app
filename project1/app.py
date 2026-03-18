from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name= request.args.get("name", "World")
    return render_template("index.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "World"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")