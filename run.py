import uvicorn
from config import PORT

if __name__=="__main__":
    uvicorn.run("First:app",reload=True,debug=True,workers=1)