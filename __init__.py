from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()
app.mount('/static',StaticFiles(directory="./First/static"),name="static")
templates=Jinja2Templates(directory="./First/templates")

from First.views import main