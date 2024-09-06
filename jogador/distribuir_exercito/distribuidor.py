import random
from jogador.preparacao import cor

valores_aleatorios = random.sample(range(1, 7), 6)

distribuidor = None

for i in range(1, 7):
    cor_atual = cor.buscar_cor(i)
    valor_atual = valores_aleatorios[i - 1]

    if valor_atual == 6 and distribuidor is None:
        distribuidor = cor_atual

    print(f"A cor {cor_atual} recebeu o valor {valor_atual}")

if distribuidor:
    print(f"\nO distribuidor e primeiro jogador é: {distribuidor}")
