from jogador.preparacao.cor import *
from jogador.preparacao.objetivos import *
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_hello():
    return "Hello world!"

@app.get("/prepara/cor")
async def get_color(select_cor:int):
    return buscar_cor(select_cor)

@app.get("/prepara/objetivo")
async def get_objetivo():
    return buscar_objetivo()

