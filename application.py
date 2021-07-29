from flask import Flask, render_template
#import pymysql.cursors
from rdkit import Chem
from rdkit.Chem import Draw 
from rdkit.Chem.Draw import rdMolDraw2D
from flask import Markup


#db = pymysql.connect(
 #   host='dci-database.capioxzatswy.ap-southeast-2.rds.amazonaws.com',
   # user='admin',
  #  password='WH4eO1nkUbsoD8a0iUXi',  
    #db="sys",
    #charset='utf8mb4',
    #)

#cursor = db.cursor()
#query = "SELECT * FROM sys.DCIDB;"
#cursor.execute(query)
#data = cursor.fetchall()

application = Flask(__name__, template_folder='template')


mol = Chem.MolFromSmiles('c1ccccc1')
d = rdMolDraw2D.MolDraw2DSVG(300, 350)
d.DrawMolecule(mol)
d.FinishDrawing()
m = d.GetDrawingText()


@application.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@application.route('/database/', methods=['GET', 'POST'])
def about():
    
    return render_template('database.html', data=Markup(m))