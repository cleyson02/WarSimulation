from jogador.preparacao.cor import *
from jogador.preparacao.objetivos import *
from jogador.jogador import Jogador
from jogador.distribuir_exercito.distribuidor_posicao import *
from jogador.distribuir_exercito.distribuidor_exercito import *
from jogador.distribuir_exercito.territorios import *
from fastapi import FastAPI, Response



app = FastAPI()

jogadores = []
ultimo_id = 0


        
@app.post("/novoJogador",summary="Entrar no jogo", description="Escolha a uma cor para ser a cor do seu exercito: 1 - AZUL; 2 - BRANCA; 3 - VERMELHA; 4 - PRETA; 5 - AMARELO; 6 - VERDE")
async def novo_jogador(select_cor:int):
    create_jogador = Jogador(ultimo_id+1,buscar_cor(select_cor),buscar_objetivo(),distribuir_terri(),pegar_posicao(jogadores,ultimo_id+1),receber_exercito_inicio())
    jogadores.append(create_jogador)
    return Response(status_code=200)

@app.get("/num-player")
async def get_playernum(id:int):
    return jogadores[id-1]

@app.get("/prepara/cor")
async def get_color(id:int):
    return jogadores[id-1].get_cor()

@app.get("/prepara/objetivo")
async def get_objetivos(id:int):
    return jogadores[id-1].get_objetivo()

@app.get("/distribui/territorio")
async def get_terri(id:int):
    return jogadores[id-1].get_territorio()

@app.get("/distribui/posicao")
async def get_posicional(id:int):
    return jogadores[id-1].get_posicao()

@app.get("/distribui/qtdexercito")
async def get_qtd_exercito_jogador(id:int):
    return jogadores[id-1].get_qtd_exercito()
