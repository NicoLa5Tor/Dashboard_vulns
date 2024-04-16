from flask import Flask,render_template
#creacion de variable flask para ejecutar
app = Flask(__name__,static_folder='Static')
@app.route('/index.html')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)