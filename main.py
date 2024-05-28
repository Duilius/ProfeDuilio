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


##########
# PRIMARIA
##########

@app.get("/primaria", response_class=HTMLResponse)
async def cursos(request:Request):
    return templates.TemplateResponse("html/primaria.html", {"request":request})

@app.get("/primaria/curso")
async def primaria2(request: Request, el_curso: str):
    print("El Curso es ====> ", el_curso)

    if el_curso == "ari":
        grado = "grados_aritmetica"
    if el_curso == "alg":
        grado = "grados_algebra"
    if el_curso == "geo":
        grado = "grados_geometria"
    if el_curso == "tri":
        grado = "grados_trigonometria"
    if el_curso == "raz":
        grado = "grados_raz_mat"
    if el_curso == "est":        
        grado = "grados_estadistica"

    #print("El Curso es ====> ", grado)
    return templates.TemplateResponse("html/"+ grado +".html", {"request":request})


@app.get("/primaria/teoria-por-grado")
async def primaria2(request: Request, curso: str, nivel:str, grado:str):
    print("El Curso es ====> ", curso)
    print("El Nivel es ====> ", nivel)

    #/primaria/teoria-por-grado?curso=ari&grado=cinco&nivel=primaria

    if grado == "cinco":
        grado="5"
        pagina = nivel+"_"+curso+"_"+grado+".html"
    if grado == "sexto":
        grado="6"
    if grado == "primero":
        grado="1"
    if grado == "segundo":
        grado="2"
    if grado == "tercero":
        grado="3"
    if grado == "cuarto":
        grado="4"
    if grado == "quinto":
        grado="5"        
    #print("El Curso es ====> ", temario)
    return templates.TemplateResponse("html/"+ nivel +"_"+ curso +"_" + grado +".html", {"request":request})

############
# SECUNDARIA
############

@app.get("/secundaria", response_class=HTMLResponse)
async def primaria(request:Request):
    return templates.TemplateResponse("html/secundaria.html", {"request":request})


############
# SECUNDARIA
############

@app.get("/preuniversitaria", response_class=HTMLResponse)
async def preuniversitaria(request:Request):
    return templates.TemplateResponse("html/preuniversitaria.html", {"request":request})

##############
#TRIGONOMETRÍA
##############
@app.get("/trigonometria", response_class=HTMLResponse)
async def trigonometria(request:Request):
    return templates.TemplateResponse("html/trigonometria.html", {"request":request})


##################
# BLOG MATEMÁTICAS
##################

@app.get("/blog-matematicas", response_class=HTMLResponse)
async def blog_matematicas(request:Request):
    return templates.TemplateResponse("html/blog/blog-matematicas.html", {"request":request})

@app.get("/tips-resumen-estudiar-matematicas", response_class=HTMLResponse)
async def tips(request:Request):
    return templates.TemplateResponse("html/blog/tips-resumen-estudiar-matematicas.html", {"request":request})

@app.get("/tips-completo-estudiar-matematicas", response_class=HTMLResponse)
async def tips(request:Request):
    return templates.TemplateResponse("html/blog/tips-completo-estudiar-matematicas.html", {"request":request})