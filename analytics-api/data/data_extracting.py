import pandas as pd
from pymongo import MongoClient

def data_extractor():
    client=MongoClient('mongodb+srv://akshathkamath:akshath@storesmartcluster.ainagbr.mongodb.net/?retryWrites=true&w=majority&appName=StoreSmartCluster')
    db=client['StoreSmartDatabase']
    collection=db['StoreSmartCollection']
    cursor = collection.find()
    data = list(cursor)
    df = pd.DataFrame(data)
    df.drop(columns=['_id'],inplace=True)
    return df