import requests
import json
from ..database.crud import  DatabaseCrud
class Nist:
    def __init__(self):
        print("Entra a crear el objeto")
        self.obj = DatabaseCrud()
        print("crea el objeto")
    def api_nist(self):
        url = 'https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex=200000'
        try:
            response = requests.get(url)    
            data = response.json()
            print(json.dumps(data['totalResults'],indent=2))
            dat = self.obj.addItem(
                container="Vulns",
                db='Nist',
                partition="Total",
                nameItem="SearchVulns",
                item=response
                )
            return data['totalResults']
        except Exception as e:
            return e
     
