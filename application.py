from flask import Flask, render_template, Markup
from rdkit import Chem
from rdkit.Chem import Draw 
from rdkit.Chem.Draw import rdMolDraw2D

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