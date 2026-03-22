from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

slots = {
    "Mahjong Ways 2": {"rtp":96.95},
    "Lucky Neko": {"rtp":96.73},
    "Fortune Tiger": {"rtp":96.81}
}

@app.get("/", response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/analyze",response_class=HTMLResponse)
def analyze(request:Request,game:str=Form(...),capital:int=Form(...)):

    bet=int(capital*0.01)
    stoploss=int(capital*0.3)
    stopwin=int(capital*0.5)

    return templates.TemplateResponse("index.html",{
        "request":request,
        "result":{
            "game":game,
            "bet":bet,
            "stoploss":stoploss,
            "stopwin":stopwin
        }
    })
