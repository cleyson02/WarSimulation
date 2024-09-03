default_colors = {
    1 : "AZUL",
    2 : "BRANCA",
    3 : "VERMELHA",
    4 : "PRETA",
    5 : "AMARELO",
    6 : "VERDE"
}

def buscar_cor(cor_solicitada):
    for i in default_colors.keys():
        if(cor_solicitada == i):
            return default_colors[i]