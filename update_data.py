#esta clase se conecta directamente con el api de nist para actualizar su base de datos y al tiempo,
#esto actualiza la base de datos, y al tiempo, esto actualiza nuestro dashboard
import requests
import threading
class Update_data:
    def __init__(self):
        self.url = 'https://nist-db.onrender.com'

    def main_update(self):
        therad = threading.Thread(target=self.update)
        therad.start()
        print('Empieza la actualizacion')
        
    def update(self):
        uril = self.url + '/update_data'
        try:
            response = requests.get(url=uril)
            return response.status_code
        except Exception as e:
            print(e)
            return 0