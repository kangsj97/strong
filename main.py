from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def 작명():
    return FileResponse('home.html')

@app.get("/join")
def 작명():
    return FileResponse('join.html')

@app.get("/main")
def 작명():
    return FileResponse('main.html')

@app.get("/find")
def 작명():
    return FileResponse('find.html')