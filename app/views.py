from flask import render_template
from app import app

@app.route('/')
def root():
    return "Hello, root!"
@app.route('/index')
def index():
    return render_template("index.html",
                           title = "home")