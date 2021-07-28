from flask import Flask, render_template
import pyodbc

application = Flask(__name__, template_folder='template')



server = 'database-1.capioxzatswy.ap-southeast-2.rds.amazonaws.com'
database = 'dci-database'
username = 'admin'
password = 'WH4eO1nkUbsoD8a0iUXi'
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM DCIDB")
        data = cursor.fetchall()

@application.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@application.route('/database/', methods=['GET', 'POST'])
def about():
    return render_template('database.html', data=data)