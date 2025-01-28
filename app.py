# Importação 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

#Modelagem de dados
class Product(db.model): 
    id = db.Columm(db.Integer, primary_key=True) 
    name = db.Column(db.string(100), nullable=False)
    prince = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True) 

# Definição de rota raiz (Pagina Incial) e função que será executada ao requisitar 
@app.route('/')
def Hello_Word(): 
    return 'Hello Word!' 

if __name__=="__main__":
    app.run(debug=True)
