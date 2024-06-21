import pandas as pd
from pymongo import MongoClient

def data_checker():
    client=MongoClient('mongodb+srv://akshathkamath:akshath@storesmartcluster.ainagbr.mongodb.net/?retryWrites=true&w=majority&appName=StoreSmartCluster')
    db=client['StoreSmartDatabase']
    collection=db['StoreSmartCollection']
    query={}
    count = collection.count_documents(query)
    return count