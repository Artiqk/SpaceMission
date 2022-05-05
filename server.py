from flask import Flask, render_template, request

from flask_mysqldb import MySQL


app = Flask(__name__)

# Configure la connexion à la base de donnée avec les identifiants + mot de passe
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'webAdmin'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'space_missions'

mysql = MySQL(app)


def htmlspecialchars (text): # Remplace les caractères spéciaux pour éviter les injections SQL
    return (text.replace("&", "&amp;").replace('"', "&quot;").replace("'", "&#039;").replace("<", "&lt;").replace(">", "&lt;"))


def getDataFromMySQLDB (request): # Initialise la connexion à la BDD et execute la requête SQL
    cursor = mysql.connection.cursor()
    sql_request = request
    cursor.execute(sql_request)
    data = cursor.fetchall()
    return data


def insertDataInMySQLDB (request):
    cursor = mysql.connection.cursor()
    message = ""
    try:
        cursor.execute(request)
        mysql.connection.commit()
        message = "<h2>La base de donnée a été mise à jour.</h2>"
    except:
        message = "<h3>La base de donnée n'a pas été mise à jour.</h3>"
    finally:
        cursor.close()

    return message


def prepareHTMLStringForTable (datas): # Prépare un code HTML pour afficher les donnnées récupérés dans un tableau
    html_data = ""

    for all_data in datas:
        html_data += "<tr>"
        for data in all_data:
            html_data += "<td>" + str(data) + "</td>"
        html_data += "</tr>"
    
    return html_data


@app.route("/") # Retourne la page html (index)
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
    missions = getDataFromMySQLDB("SELECT mission_name, mission_description FROM missions;")

    html_data = prepareHTMLStringForTable(missions)

    return render_template('display_missions.html', data=html_data)


@app.route('/display_users')
def display_users():
    users = getDataFromMySQLDB("SELECT first_name, last_name, age, mail FROM users;")

    html_data = prepareHTMLStringForTable(users)

    return render_template('display_users.html', data=html_data)


@app.route('/create_missions', methods=['GET', 'POST'])
def create_missions (): 
    post_data_name = ['mission_name', 'mission_desc']

    message = insertDataInMySQLDB("INSERT INTO missions(mission_name, mission_description) VALUES('" + htmlspecialchars(request.form[post_data_name[0]]) + "','" + htmlspecialchars(request.form[post_data_name[1]]) + "');")

    return render_template('create_mission.html', data=message)
    

@app.route('/create_users', methods=['GET', 'POST'])
def create_users (): 
    post_data_name = ['first_name', 'last_name', 'age', 'mail']

    message = insertDataInMySQLDB("INSERT INTO users(first_name, last_name, age, mail) VALUES('" + htmlspecialchars(request.form[post_data_name[0]]) + "','" + htmlspecialchars(request.form[post_data_name[1]]) + "'," + htmlspecialchars(request.form[post_data_name[2]]) + ",'" + htmlspecialchars(request.form[post_data_name[3]]) + "');")

    return render_template('create_user.html', data=message)