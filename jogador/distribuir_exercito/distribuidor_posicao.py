from random import randint
from jogador.preparacao.cor import buscar_cor

def pegar_posicao(jogadores,id):
    posicao = verificar_posicao(jogadores,sorteio())
    return posicao

def verificar_posicao(lista_jogadores,posicao):
    for i in lista_jogadores:
        if(i.get_posicao == posicao):
            verificar_posicao(lista_jogadores,sorteio())
    return posicao


def sorteio():
    return randint(1, 6)



