from flask import Flask, render_template, request
import os

from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'webAdmin'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'space_missions'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create_mission')
def create_mission ():
    return render_template('create_mission.html')

@app.route('/create_user')
def create_user ():
    return render_template('create_user.html')

@app.route('/create_missions', methods=['GET', 'POST'])
def create_missions (): 
    post_data_name = ['mission_name', 'mission_desc']
    sql_request = "INSERT INTO missions(mission_name, mission_description) VALUES('" + request.form[post_data_name[0]] + "','" + request.form[post_data_name[1]] + "');"
    cursor = mysql.connection.cursor()
    cursor.execute(sql_request)
    mysql.connection.commit()
    cursor.close()  
    return "<p>" + sql_request + "</p>"

@app.route('/create_users', methods=['GET', 'POST'])
def create_users (): 
    post_data_name = ['first_name', 'last_name', 'age', 'mail']
    sql_request = "INSERT INTO users(first_name, last_name, age, mail) VALUES('" + request.form[post_data_name[0]] + "','" + request.form[post_data_name[1]] + "'," + request.form[post_data_name[2]] + ",'" + request.form[post_data_name[3]] + "');"
    cursor = mysql.connection.cursor()
    cursor.execute(sql_request)
    mysql.connection.commit()
    cursor.close()  
    return "<p>" + sql_request + "</p>"