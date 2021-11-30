from flask import Flask, render_template, request
import datetime
 
app = Flask(__name__)

entries = []

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")  #content is the name of the html field (request.form behaves like a dictionary)4

        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")

        entries.append((entry_content, formatted_date))


    return render_template("home.html", entries = entries)