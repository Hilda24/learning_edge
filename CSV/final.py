from fastapi import FastAPI, File, UploadFile

import pandas as pd
app=FastAPI()

@app.post("/uploadcsv/")
def upload_csv(csv_file: UploadFile = File(...)):
    dataframe = pd.read_csv(csv_file.file)
    dataframe1=pd.to_numeric(dataframe['Name'], errors='coerce')
    dataframe1=dataframe.fillna(0)
    head1=dataframe1.to_json(orient='records')
    return {"filename": head1}

