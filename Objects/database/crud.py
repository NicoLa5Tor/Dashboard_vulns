import requests,datetime
import json


class DatabaseCrud:
    
    #constructor, con el self se pueden hacer llamadas en cualquier metodo desde que se 
    #inicialise en el constructo, cabe recalcar que los metodos tambien deben pedir la variable self
    #
    def __init__(self):
         self.url_basic = self.url()
    #trae la url de config.json 
    def url(self):
        with open('config.json','r') as conf:
            conf_data = json.load(conf)
            return conf_data['urlCosmos'] 

    #agregar item
    def addItem(self,item,db,container,nameItem,partition):
        data = {
            "name_Db" : db,
            "name_item" : nameItem,
            "partition" : partition,
            "container" : container,
            "item" : item
        }
        try:           
            response = requests.post(self.url_basic+"create_item",json=data)
            return f"Item {item} gradado con exito en la base {db} "
        except Exception as e:
            print(f"Error al guardar el item: {e}")
            return None
    #traer item específico
    def getItem(self,db,container,nameItem,partition):
        data={
            "name_Db":db,
            "container" : container,
            "name_item" : nameItem,
            "partition" : partition
        }
        try: 
            response = requests.get(self.url_basic+"get_item",json=data)
            return response.json()
        except Exception as e:
            print(f"Error al consultar el item {nameItem}: {e}")
            return None
    #eliminar base de datos
    def deleteDatabase(self,db):
        data = {
            "name_Db": db
        }
        try:
            reponse = requests.delete(self.url_basic+"delete_database",json=data)
            return reponse.json()
        except Exception as e:
            print(f"Error a eliminar la base de datos: {e}")
            return e
    #consulatar items creados
    def list_items(self,db,container):
        data ={
            "name_Db": db,
            "container" : container
        }
        try:
            response = requests.get(self.url_basic+"list_items",json=data)
            return response.json()

        except Exception as e:
            print(f"Error al consultar el item {db}: {e}")
            

