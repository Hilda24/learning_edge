from fastapi import FastAPI,File,UploadFile
from new import convertBytesTostring
app=FastAPI()
@app.post("/csv/")
async def parsecsv(file:UploadFile=File(...)):
    contents=await file.read()
    json_string=convertBytesTostring(contents)
    return {"file-contents":json_string}
