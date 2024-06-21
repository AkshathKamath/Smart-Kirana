import pandas as pd
from pymongo import MongoClient

def data_deleter():
    client=MongoClient('mongodb+srv://akshathkamath:akshath@storesmartcluster.ainagbr.mongodb.net/?retryWrites=true&w=majority&appName=StoreSmartCluster')
    db=client['StoreSmartDatabase']
    collection=db['StoreSmartCollection']
    result = collection.delete_many({})
    # print(f'Deleted {result.deleted_count} documents.')