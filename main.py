from flask import Flask, render_template, jsonify
from update_data import Update_data
import requests
import json

# Crear una instancia de Flask
app = Flask(__name__, static_folder='Static')
# Ruta para servir la página principal
@app.route('/')
def index():
    abj_update = Update_data()
    abj_update.main_update()
    
    return render_template('index.html')  

# Función para buscar datos en la base de datos
def search_db():
    # Datos de ejemplo para la consulta
    data = {
        "name_db": "NicolasJuan",
        "_id": "Count_Vulns",
        "name_collection": "Content"
    }
    try:
        # URL del servicio de consulta a la base de datos
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

# Ruta para obtener datos desde la API
@app.route('/api/data')
def get_data():
    data = search_db()
    return jsonify({"response": {"item": data}})

# Ruta para datos de ejemplo de una gráfica
def search3_db():
    data = {
        "name_db": "NicolasJuan",
        "_id": "Info_Machines",
        "name_collection": "Content"
    }
    try:
        url = "https://mongoatlas-crxv.onrender.com/get_item"
        response = requests.get(url, json=data, timeout=10)  # Añadir un tiempo de espera de 10 segundos

        if response.status_code == 200:
            dat = response.json()
            print(json.dumps(dat, indent=4))  # Imprimir la respuesta completa en formato JSON con indentación
            return dat.get('response', {}).get('item', {}).get('Top10_Machinas', {})
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.Timeout:
        print("La solicitud a la API ha expirado.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la base en busca del item: {str(e)}")
        return None

def search3_db():
    data = {
        "name_db": "NicolasJuan",
        "_id": "Info_Machines",
        "name_collection": "Content"
    }
    try:
        url = "https://mongoatlas-crxv.onrender.com/get_item"
        response = requests.get(url, json=data, timeout=10)  # Añadir un tiempo de espera de 10 segundos

        if response.status_code == 200:
            dat = response.json()
            print(json.dumps(dat, indent=4))  # Imprimir la respuesta completa en formato JSON con indentación
            return dat.get('response', {}).get('item', {}).get('Top10_Machinas', {})
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.Timeout:
        print("La solicitud a la API ha expirado.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la base en busca del item: {str(e)}")
        return None

@app.route('/data')
def data():
    top_machines = search3_db()
    
    if not top_machines:
        return jsonify({"error": "No se encontraron los datos o ocurrió un error."}), 500

    labels = []
    critical_data = []
    high_data = []
    medium_data = []
    low_data = []

    for machine, vulnerabilities in top_machines.items():
        labels.append(machine)
        critical_data.append(vulnerabilities.get('Critical', 0))
        high_data.append(vulnerabilities.get('High', 0))
        medium_data.append(vulnerabilities.get('Medium', 0))
        low_data.append(vulnerabilities.get('Low', 0))

    datos = {
        'labels': labels,
        'datasets': [
            {'label': 'Critical', 'data': critical_data, 'backgroundColor': 'rgba(0, 0, 0, 0.6)', 'borderColor': 'rgba(0, 0, 0, 1)', 'borderWidth': 1},
            {'label': 'High', 'data': high_data, 'backgroundColor': 'rgba(220, 53, 69, 0.6)', 'borderColor': 'rgba(220, 53, 69, 1)', 'borderWidth': 1},
            {'label': 'Medium', 'data': medium_data, 'backgroundColor': 'rgba(255, 159, 64, 0.6)', 'borderColor': 'rgba(255, 159, 64, 1)', 'borderWidth': 1},
            {'label': 'Low', 'data': low_data, 'backgroundColor': 'rgba(255, 193, 7, 0.6)', 'borderColor': 'rgba(255, 193, 7, 1)', 'borderWidth': 1}
        ]
    }
    
    return jsonify(datos)

# Función para buscar datos de vulnerabilidades por mes en la base de datos
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

# Ruta para obtener datos de vulnerabilidades por mes
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

# Ruta para obtener datos de población
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

def search4_db():
    data = {
        "name_db": "NicolasJuan",
        "_id": "Info_Machines",
        "name_collection": "Content"
    }
    try:
        url = "https://mongoatlas-crxv.onrender.com/get_item"
        response = requests.get(url, json=data, timeout=10)  # Añadir un tiempo de espera de 10 segundos

        if response.status_code == 200:
            dat = response.json()
            print(json.dumps(dat, indent=4))  # Imprimir la respuesta completa en formato JSON con indentación
            item = dat.get('response', {}).get('item', {})
            mas_vuln = item.get('Menos_Mas', {}).get('mas_vuln', None)
            menos_vuln = item.get('Menos_Mas', {}).get('menos_vuln', None)
            total_vulns = item.get('Total_Vulns', None)
            return mas_vuln, menos_vuln, total_vulns
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None, None, None

    except requests.exceptions.Timeout:
        print("La solicitud a la API ha expirado.")
        return None, None, None
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la base en busca del item: {str(e)}")
        return None, None, None

@app.route('/data5')
def data5():
    _, _, total_vulns = search4_db()
    if total_vulns is not None:
        return jsonify({'total_vulnerabilities': total_vulns})
    else:
        return jsonify({"error": "No se encontraron los datos o ocurrió un error."}), 500

@app.route('/data6')
def data6():
    mas_vuln, _, _ = search4_db()
    if mas_vuln is not None:
        return jsonify({'machine_name': mas_vuln})
    else:
        return jsonify({"error": "No se encontraron los datos o ocurrió un error."}), 500

@app.route('/data7')
def data7():
    _, menos_vuln, _ = search4_db()
    if menos_vuln is not None:
        return jsonify({'machine_name': menos_vuln})
    else:
        return jsonify({"error": "No se encontraron los datos o ocurrió un error."}), 500

def search2_db():
    data = {
        "name_db": "NicolasJuan",
        "_id": "Top_CVE",
        "name_collection": "Content"
    }
    try:
        url = "https://mongoatlas-crxv.onrender.com/get_item"
        response = requests.get(url=url, json=data)
        
        if response.status_code == 200:
            dat = response.json()
            return dat.get('response', {}).get('item', None)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"Error al consultar la base en busca del item: {str(e)}")
        return None

@app.route('/top-vulnerabilities', methods=['GET'])
def top_vulnerabilities():
    item = search2_db()
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "No se encontró el item o ocurrió un error."}), 404

# Ruta para obtener detalles de un CVE específico
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

# Ejecutar la aplicación en modo debug
if __name__ == '__main__':
    app.run(debug=True)
