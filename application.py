from flask import Flask, render_template, Markup


application = Flask(__name__, template_folder='template')




@application.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@application.route('/database/', methods=['GET', 'POST'])
def about():
    
    return render_template('database.html', data="hi")