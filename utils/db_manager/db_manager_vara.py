
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv() 

class VaraDBManager:
    def __init__(self):
        """
        Initializes the GraphicDBManager with a MongoDB database instance.
        """
        # Connection to the MongoDB instance
        client = MongoClient(os.getenv('MONGOATLAS_VARA'))
        self.db = client.VaraNetwork  # Connection to the 'coinmetrics' database
    
    def get_blockDetails_events(self):
        """
        Returns a list of metric events, including the 'now' field.
        """
        # Actualiza esta línea para incluir la lógica adecuada
        return list(self.db.vara.find({}, {'_id': 0, 'blockDetails': 1, 'events': 1}))
    
    def get_last_three_documents(self):
        """
        Retorna los últimos tres documentos de la colección.
        """
        # Suponiendo que quieres ordenar por un campo de marca de tiempo. Si no existe, puedes usar '_id'.
        # -1 en sort() indica orden descendente
        return list(self.db.vara.find({}, {'_id': 0}).sort('_id', -1).limit(3))
        