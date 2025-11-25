from flask import Flask, render_template
from context import services, testimonials, consultations

app = Flask(__name__)


@app.get("/")
def GET_index():
    return render_template("index.html", services=services, testimonials=testimonials, consultations=consultations)
