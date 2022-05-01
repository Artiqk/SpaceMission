from flask import Flask, render_template
import os


project_path = os.path.dirname(__file__)

app = Flask(__name__, template_folder=project_path)

@app.route("/")

def index():
    return render_template('index.html')