from crud import DatabaseCrud
import json
#este archivo es único y explusivo para testing, no se llama en ninguna otra clase
obj = DatabaseCrud()

def getIt():
    dat =obj.getItem(container="datos",db='Nist',nameItem="prueba",partition='1')
    print(dat['status'])
def deleteDB(nameDb):
    delet = obj.deleteDatabase(db=nameDb)
    print(delet)
def listItems():
    li = obj.list_items(container="Vulns",db="Nist")
    print(json.dumps(li['response'],indent=2))
listItems()

#deleteDB("prueba1")