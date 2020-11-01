import pandas as pd 
import json

def convertBytesTostring(bytes):
    data=bytes.decode('utf-8').splitlines()
    df=pd.DataFrame(data)
    print(df.dtypes)
    return parse_csv(df)

def parse_csv(df):
    result=df.to_json(orient="records")
    parsed=json.loads(result)
    return parsed