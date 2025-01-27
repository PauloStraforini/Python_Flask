# Importação 
from flask import Flask 

app = Flask(__name__)

# Definição de rota raiz (Pagina Incial) e função que será executada ao requisitar 
@app.route('/')
def Hello_Word(): 
    return 'Hello Word!' 

if __name__=="__main__":
    app.run(debug=True)
    