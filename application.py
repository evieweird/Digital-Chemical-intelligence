from flask import Flask, render_template
import pymysql
import re

application = Flask(__name__, template_folder='template')

host='dci-database.capioxzatswy.ap-southeast-2.rds.amazonaws.com'
user = 'admin'
password = 'WH4eO1nkUbsoD8a0iUXi'
db = 'dci-database'

con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
       
cur = con.cursor()
cur.execute("SELECT * FROM dataset")
data = cur.fetchall()

@application.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@application.route('/database/', methods=['GET', 'POST'])
def about():
    return render_template('database.html', data=data)