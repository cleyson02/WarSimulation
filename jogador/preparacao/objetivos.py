
from random import randint
objetivos = {
1:"Conquistar na totalidade a EUROPA, a OCEANIA e mais um terceiro.",
2:"Conquistar na totalidade a ÁSIA e a AMÉRICA DO SUL.",
3:"Conquistar na totalidade a EUROPA, a AMÉRICA DO SUL e mais um terceiro.",
4:"Conquistar 18 TERRITÓRIOS e ocupar cada um deles com pelo menos dois exércitos.",
5:"Conquistar na totalidade a ÁSIA e a ÁFRICA.",
6:"Conquistar na totalidade a AMÉRICA DO NORTE e a ÁFRICA.",
7:"Conquistar 24 TERRITÓRIOS à sua escolha.",
8:"Conquistar na totalidade a AMÉRICA DO NORTE e a OCEANIA.",
9:"Destruir totalmente OS EXÉRCITOS AZUIS.",
10:"Destruir totalmente OS EXÉRCITOS AMARELOS.",
11:"Destruir totalmente OS EXÉRCITOS VERMELHOS.",
12:"Destruir totalmente OS EXÉRCITOS PRETOS.",
13:"Destruir totalmente OS EXÉRCITOS BRANCO.",
14:"Destruir totalmente OS EXÉRCITOS VERDES"
}

def buscar_objetivo():
    value = randint(1,14)
    return objetivos[value]
