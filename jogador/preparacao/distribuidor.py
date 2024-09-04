import random
import cor

# Gerando uma lista de números aleatórios de 1 a 6 sem repetição
valores_aleatorios = random.sample(range(1, 7), 6)

# Variável para armazenar a cor que receber o valor 6 primeiro
distribuidor = None

# Atribuindo valores aleatórios às cores
for i in range(1, 7):
    cor_atual = cor.buscar_cor(i)
    valor_atual = valores_aleatorios[i - 1]
    
    # Verifica se o valor é 6 e atribui à variável 'distribuidor'
    if valor_atual == 6 and distribuidor is None:
        distribuidor = cor_atual
    
    print(f"A cor {cor_atual} recebeu o valor {valor_atual}")

# Exibindo o 'distribuidor'
if distribuidor:
    print(f"\nO distribuidor e primeiro jogador é: {distribuidor}")
