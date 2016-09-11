from flask import Flask, redirect, render_template, request, url_for                             
app = Flask(__name__)

app.config["DEBUG"] = True



@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "GET":
        return render_template("main_page.html")

choice = request.form["choice"]
equation = request.form["equation"]
return redirect(url_for("answer_page.html")   
