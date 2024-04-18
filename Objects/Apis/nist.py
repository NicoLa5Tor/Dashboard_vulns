import requests
import json

class Nist:
    def api_nist(self):
        url = 'https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex=200000'
        try:
            response = requests.get(url)    
            data = response.json()
            #print(json.dumps(data['totalResults'],indent=2))
            return data['totalResults']
        except Exception as e:
            return e
