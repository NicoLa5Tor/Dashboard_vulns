from flask import Flask,render_template
from Objects.Apis.nist import Nist

#creacion de objetos
nist = Nist()
#creacion de variable flask para ejecutar
app = Flask(__name__,static_folder='Static')
@app.route('/index.html')
def index():
    data = nist.api_nist()
    return render_template('index.html', data = data)
if __name__ == '__main__':
    app.run(debug=True, port=8080)