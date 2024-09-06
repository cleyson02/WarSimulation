from jogador.preparacao.cor import *
from jogador.preparacao.objetivos import *
from jogador.jogador import Jogador
from jogador.distribuir_exercito.territorios import *
from fastapi import FastAPI
app = FastAPI()


jogadores = []

@app.post("/novoJogador",summary="Entrar no jogo", description="Escolha a uma cor para ser a cor do seu exercito: 1 - AZUL; 2 - BRANCA; 3 - VERMELHA; 4 - PRETA; 5 - AMARELO; 6 - VERDE")
def novo_jogador(select_cor:int):
    create_jogador = Jogador(buscar_cor(select_cor),buscar_objetivo(),distribuir_terri())
    jogadores.append(create_jogador)
    return 

@app.get("/num-player")
async def get_playernum(id:int):
    return jogadores[id]

@app.get("/prepara/cor")
async def get_color(id:int):
    return jogadores[id].get_cor()

@app.get("/prepara/objetivo")
async def get_objetivos(id:int):
    return jogadores[id].get_objetivo()

@app.get("/distribui/territorio")
async def get_terri(id:int):
    return jogadores[id].get_territorio()

@app.get("/distribui/posicao")
async def get_posicao(id:int):
    return 0

