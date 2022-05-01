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

@app.route('/display_missions')
def display_missions():
    cursor = mysql.connection.cursor()
    sql_request = "SELECT mission_name, mission_description FROM missions;"
    cursor.execute(sql_request)
    missions = cursor.fetchall()

    html_data = ""

    for all_missions in missions:
        html_data += "<tr>"
        for mission in all_missions:
            html_data += "<td>" + str(mission) + "</td>"
        html_data += "</tr>"

    return render_template('display_missions.html', data=html_data)

@app.route('/display_users')
def display_users():
    cursor = mysql.connection.cursor()
    sql_request = "SELECT first_name, last_name, age, mail FROM users;"
    cursor.execute(sql_request)
    users = cursor.fetchall()

    html_data = ""

    print(users)

    for all_user in users:
        html_data += "<tr>"
        for user in all_user:
            html_data += "<td>" + str(user) + "</td>"
        html_data += "</tr>"

    return render_template('display_users.html', data=html_data)

@app.route('/create_missions', methods=['GET', 'POST'])
def create_missions (): 
    post_data_name = ['mission_name', 'mission_desc']
    sql_request = "INSERT INTO missions(mission_name, mission_description) VALUES('" + request.form[post_data_name[0]] + "','" + request.form[post_data_name[1]] + "');"
    cursor = mysql.connection.cursor()
    cursor.execute(sql_request)
    mysql.connection.commit()
    cursor.close()  
    return render_template('create_mission.html')

@app.route('/create_users', methods=['GET', 'POST'])
def create_users (): 
    post_data_name = ['first_name', 'last_name', 'age', 'mail']
    sql_request = "INSERT INTO users(first_name, last_name, age, mail) VALUES('" + request.form[post_data_name[0]] + "','" + request.form[post_data_name[1]] + "'," + request.form[post_data_name[2]] + ",'" + request.form[post_data_name[3]] + "');"
    cursor = mysql.connection.cursor()
    cursor.execute(sql_request)
    mysql.connection.commit()
    cursor.close()  
    return render_template('create_user.html')