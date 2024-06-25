import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

def data_extractor():
    load_dotenv()

    MONGO_URL = os.getenv('MONGO_URL')
    DB_NAME = os.getenv('DB_NAME')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME')

    client=MongoClient(MONGO_URL)
    db=client[DB_NAME]
    collection=db[COLLECTION_NAME]
    
    cursor = collection.find()
    data = list(cursor)
    df = pd.DataFrame(data)
    df.drop(columns=['_id'],inplace=True)
    client.close()
    return df