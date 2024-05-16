from flask import Flask, render_template, jsonify, request
import matplotlib.pyplot as plt
import requests,json

app = Flask(__name__, static_folder='Static')

@app.route('/index.html')
def index():
    return render_template('index.html')

def search_db():
    data = {
        "name_db": "NicolasJuan",
        "_id": "Count_Vulns",
        "name_collection": "Content"
    }
    try:
        url = "https://mongoatlas-crxv.onrender.com/get_item"
        response = requests.get(url=url, json=data)
        if response.status_code == 200:
            dat = response.json()
            return dat['response']['item']
        else:
            print("Error de acceso al consultar")
            return None
    except Exception as e:
        print(f"Error al consultar la base para en busca del item {str(e)}")
        return None
    
@app.route('/api/data')
def get_data():
    data = search_db()
    return jsonify({"response": {"item": data}})


@app.route('/data')

def data():
    datos = {
        'labels': ['PC 1', 'PC 2', 'PC 3', 'PC 4', 'PC 5', 'PC 6', 'PC 7', 'PC 8', 'PC 9', 'PC 10'],
        'datasets': [
            {'label': 'Critical', 'data': [400, 600, 100, 300, 600, 200, 900, 1100, 200, 500], 'backgroundColor': 'rgba(0, 0, 0, 0.6)', 'borderColor': 'rgba(0, 0, 0, 1)', 'borderWidth': 1},
            {'label': 'High', 'data': [500, 100, 200, 200, 200, 100, 100, 200, 300, 400], 'backgroundColor': 'rgba(220, 53, 69, 0.6)', 'borderColor': 'rgba(220, 53, 69, 1)', 'borderWidth': 1},
            {'label': 'Medium', 'data': [200, 300, 100, 400, 300, 700, 400, 300, 200, 100], 'backgroundColor': 'rgba(255, 159, 64, 0.6)', 'borderColor': 'rgba(255, 159, 64, 1)', 'borderWidth': 1},
            {'label': 'Low', 'data': [100, 400, 300, 200, 100, 400, 200, 600, 100, 200], 'backgroundColor': 'rgba(255, 193, 7, 0.6)', 'borderColor': 'rgba(255, 193, 7, 1)', 'borderWidth': 1},
            {'label': 'Sin Catalogar', 'data': [700, 600, 500, 300, 400, 300, 300, 500, 400, 300], 'backgroundColor': 'rgba(128, 128, 128, 0.6)', 'borderColor': 'rgba(128, 128, 128, 1)', 'borderWidth': 1}

        ]
    }
    return jsonify(datos)


def search1_db():
    data = {
        "name_db": "NicolasJuan",
        "_id": "Vulns_Per_Month",
        "name_collection": "Content"
    }
    
    url = "https://mongoatlas-crxv.onrender.com/get_item"
    
    try:
        response = requests.get(url=url, json=data)
        if response.status_code == 200:
            dat = response.json()
            print("Datos obtenidos de la API:", json.dumps(dat, indent=4))  # Mensaje de depuración
            return dat['response']['item']
        else:
            print(f"Error de acceso al consultar. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al consultar la base en busca del item: {str(e)}")
        return None

@app.route('/data2')
def data2():
    vulnerabilities = search1_db()
    if vulnerabilities is None:
        return jsonify({"error": "No se pudieron obtener los datos de la API"}), 500

    # Transformar los datos para el formato de la gráfica
    transformed_data = []
    for year, months in vulnerabilities.items():
        for month, value in months.items():
            transformed_data.append({
                'mes': f"{year}-{month}",
                'valor': value
            })
    print("Datos transformados:", transformed_data)  # Mensaje de depuración
    return jsonify(transformed_data)

@app.route('/data3')
def data3():
    poblacion = {
        'Funza': 1,
        'Mosquera': 8,
        'Madrid': 6,
        'Facatativá': 4
    }

    datos = {
        'labels': list(poblacion.keys()),
        'datasets': [
            {
                'label': 'Población',
                'data': list(poblacion.values()),
                'backgroundColor': [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    'rgba(75, 192, 192, 0.5)'
                ],
                'borderColor': [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                'borderWidth': 1
            }
        ]
    }

    return jsonify(datos)

@app.route('/data5')
def data5():
    # Datos de ejemplo para el total de vulnerabilidades
    return jsonify({'total_vulnerabilities': 45367})

@app.route('/data6')
def data6():
    # Datos de ejemplo para la máquina más vulnerable
    return jsonify({'machine_name': 'Jdmoo-X123'})
@app.route('/data7')
def data7():
    # Nueva función para la máquina menos vulnerable
    return jsonify({'machine_name': 'LessVuln Machine01'})

# Datos simulados para el ejemplo, deberías reemplazar esto con una consulta a tu base de datos
vulnerabilities = [
    {"name": "CVE-2021-34527", "severity": 9.8, "description": "Vulnerability in Windows Print Spooler Components."},
    {"name": "CVE-2021-44228", "severity": 10.0, "description": "Log4Shell vulnerability affecting Apache Log4j2."},
    {"name": "CVE-2021-30860", "severity": 9.7, "description": "Apple iOS and macOS zero-click vulnerability."},
    {"name": "CVE-2021-4034", "severity": 9.8, "description": "PwnKit: Local Privilege Escalation vulnerability in Polkit."},
    {"name": "CVE-2021-21972", "severity": 9.8, "description": "Remote code execution vulnerability in VMware vSphere Client."},
    {"name": "CVE-2021-26084", "severity": 9.8, "description": "Confluence Server Webwork OGNL injection."},
    {"name": "CVE-2021-44228", "severity": 10.0, "description": "Remote code execution in Apache Log4j2."},
    {"name": "CVE-2022-2184", "severity": 9.8, "description": "Critical SQL injection vulnerability."},
    {"name": "CVE-2022-30190", "severity": 9.8, "description": "Microsoft Support Diagnostic Tool Vulnerability."},
    {"name": "CVE-2022-22965", "severity": 9.8, "description": "Spring4Shell vulnerability in Spring Framework."}
]

@app.route('/top-vulnerabilities')
def top_vulnerabilities():
    # Simulando una respuesta de la API con los datos
    return jsonify(vulnerabilities)

@app.route('/api/cve/<cve_id>', methods=['GET'])
def api_cve(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cvss_score = data.get('cvss', 'No disponible')  # Asumiendo que cvss viene directamente en la respuesta principal
        return jsonify({'data': data, 'cvss_score': cvss_score})
    else:
        return {'error': 'CVE no encontrado'}, 404

if __name__ == '__main__':
    app.run(debug=True)

