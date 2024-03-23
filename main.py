from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates"), name="static")
templates = Jinja2Templates(directory="templates")


#######
# RUTAS
#######

@app.get("/inicio", response_class=HTMLResponse)
async def inicio(request:Request):
    return templates.TemplateResponse("html/inicio.html", {"request":request})