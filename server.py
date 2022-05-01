from django.shortcuts import render
from flask import Flask, render_template
import os


project_path = os.path.dirname(__file__)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create_mission')
def create_mission ():
    return render_template('create_mission.html')

@app.route('/create_user')
def create_user ():
    return render_template('create_user.html')