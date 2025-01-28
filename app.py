# Importação
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Modelagem
# Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


@app.route('/api/products/add', methods=['POST'])
def add_product(): 
    data = request.json
    product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
    db.session.add(product)
    db.session.commit()
    return "Produto cadastrado com sucesso!" 

# Definição de rota raiz (Pagina Incial) e função que será executada ao requisitar 
@app.route('/')
def Hello_Word(): 
    return 'Hello Word!' 

if __name__=="__main__":
    app.run(debug=True)
