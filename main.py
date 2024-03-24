## Importing the Modules Needed to Communicate Backend and Frontend.
import uvicorn
from fastapi.responses import JSONResponse, HTMLResponse
import asyncio
from fastapi import APIRouter
import os
from os import getcwd
from fastapi import FastAPI, UploadFile, Request, Response,Form,File,Header, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Optional


app = FastAPI()

app.mount("/static", StaticFiles(directory="templates"), name="static")
templates = Jinja2Templates(directory="templates")


#######
# RUTAS
#######

@app.get("/", response_class=HTMLResponse)
async def inicio(request:Request):
    return templates.TemplateResponse("html/inicio.html", {"request":request})