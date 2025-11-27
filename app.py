from flask import Flask, render_template, request
from datetime import datetime
from tinydb import TinyDB, Query
import json

app = Flask(__name__)


@app.get("/")
def GET_index():
    return render_template("index.html")


@app.get("/consultation")
def GET_consultation():
    with open('data/consultations.json', 'r') as file:
        consultations = json.load(file)
        return render_template("consultation.html", consultations=consultations)

    return "", 500


@app.get("/about")
def GET_about():
    return render_template("about.html")


@app.get("/testimonials")
def GET_testimonials():
    db = TinyDB('data/testimonials.json')
    testimonials = db.all()
    return render_template("testimonials.html", testimonials=testimonials)


@app.get("/blog")
def GET_blog():
    return render_template("blog.html")


@app.post('/write-review')
def POST_write_review():
    name = request.form["Name"]
    review_text = request.form["ReviewText"]
    db = TinyDB('data/testimonials.json')
    db.insert({"author": name, "message": review_text,
              "timestamp": datetime.now().isoformat()})
    print(name, review_text)
    return render_template("server_message.html", message="Thank You! Your review has been submitted.")
