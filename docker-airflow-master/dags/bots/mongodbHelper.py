import pymongo
def get_connection():
    db_name=None
    try:

       connection_url=pymongo.MongoClient("mongodb://localhost:27017/")
       db_name=connection_url["automation_config"]
       print(db_name)
    except Exception as exception:
       print (exception)
    return db_name

def insert_single_document(collection_name,query,projection=None):
    collection_data=None
    try:
       db_name=get_connection()
       collection_name=db_name[collection_name]
       print(collection_name)
       collection_data=collection_name.insert_one(query,projection)
       print(collection_data)
    except Exception as execption:
       print(execption)
    return collection_data


def get_single_document(collection_name,query,projection=None):
    collection_data=None
    try:
       db_name=get_connection()
       collection_name=db_name[collection_name]
       print(collection_name)
       collection_data=collection_name.find_one(query,projection)
     #  print(collection_data)
    except Exception as execption:
       print(execption)
    return collection_data

if __name__=="__main__":
   get_single_document("config",{"name":"email_config"},{"_id":0,"name":0})


def update_single_document(collection_name,query,projection=None):
    collection_data=None
    try:
       db_name=get_connection()
       collection_name=db_name[collection_name]
       print(collection_name)
       collection_data=collection_name.update_one(query,projection)
       print(collection_data)
    except Exception as execption:
       print(execption)
    return collection_data

