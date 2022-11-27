import pymongo
import pandas as pd
import json 

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

DATA_FILE_PATH ="/config/workspace/aps_failure_training_set1.csv" 
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows & Columns: {df.shape}")

    # convert df to json for dumping @ mongodb
    df.reset_index(drop = True, inplace = True)
    
    # We have to transpose the data to ?
    json_record = list(json.loads(df.T.to_json()).values())

    # print the recored
    print(json_record[0])

    # inserting the json inside mongo
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    


 