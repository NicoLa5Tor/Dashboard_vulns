from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='Static')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    datos = {
        'labels': ['PC 1', 'PC 2', 'PC 3', 'PC 4', 'PC 5', 'PC 6', 'PC 7', 'PC 8', 'PC 9', 'PC 10'],
        'datasets': [
            {'label': 'Low', 'data': [100, 400, 300, 200, 100, 400, 200, 600, 100, 200], 'backgroundColor': 'rgba(255, 99, 132, 0.5)', 'borderColor': 'rgba(255, 99, 132, 1)', 'borderWidth': 1},
            {'label': 'Medium', 'data': [200, 300, 100, 400, 300, 700, 400, 300, 200, 100], 'backgroundColor': 'rgba(54, 162, 235, 0.5)', 'borderColor': 'rgba(54, 162, 235, 1)', 'borderWidth': 1},
            {'label': 'High', 'data': [500, 100, 200, 200, 200, 100, 100, 200, 300, 400], 'backgroundColor': 'rgba(255, 206, 86, 0.5)', 'borderColor': 'rgba(255, 206, 86, 1)', 'borderWidth': 1},
            {'label': 'Critical', 'data': [400, 600, 100, 300, 600, 200, 900, 1100, 200, 500], 'backgroundColor': 'rgba(75, 192, 192, 0.5)', 'borderColor': 'rgba(75, 192, 192, 1)', 'borderWidth': 1},
            {'label': 'Sin Catalogar', 'data': [700, 600, 500, 300, 400, 300, 300, 500, 400, 300], 'backgroundColor': 'rgba(153, 102, 255, 0.5)', 'borderColor': 'rgba(153, 102, 255, 1)', 'borderWidth': 1}
        ]
    }
    return jsonify(datos)

@app.route('/data2')
def data2():
    vulnerabilities = [
        {'mes': 'Mayo 2023', 'valor': 125678},
        {'mes': 'Junio 2023', 'valor': 196759},
        {'mes': 'Julio 2023', 'valor': 35445},
        {'mes': 'Agosto 2023', 'valor': 57845},
        {'mes': 'Septiembre 2023', 'valor': 24783},
        {'mes': 'Octubre 2023', 'valor': 32346},
        {'mes': 'Noviembre 2023', 'valor': 82323},
        {'mes': 'Diciembre 2023', 'valor': 10352},
        {'mes': 'Enero 2024', 'valor': 15128},
        {'mes': 'Febrero 2024', 'valor': 91456},
        {'mes': 'Marzo 2024', 'valor': 6312},
        {'mes': 'Abril 2024', 'valor': 73456}
    ]
    return jsonify(vulnerabilities)

if __name__ == '__main__':
    app.run(debug=True)
