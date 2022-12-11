
"""
Pontuação:
Escolhe se uma pontuação de cada grupo somando as, obtendo assim a pontuaçao da ronda

jogadaFeita:
1 -> Pedra [A ou X] 
2 -> Papel [B ou Y]
3 -> Tesoura [C ou Z]

+ 

PontuaçaoRonda:
0 -> perdi a ronda
3 -> empatei a ronda 
6 -> ganhei a ronda

Ou seja,

Casos em que sou Vencido:
Adversario          Eu          Pontuação (jogadaFeita + PontuaçaoRonda)
    A                Z                          (3 + 0)
    B                X                          (1 + 0)
    C                Y                          (2 + 0)

Casos em que eu Venço:
Adversario          Eu          Pontuação (jogadaFeita + PontuaçaoRonda)
    A                Y                          (2 + 6)
    B                Z                          (3 + 6)
    C                X                          (1 + 6)


Casos em que eu Empato:
Adversario          Eu          Pontuação (jogadaFeita + PontuaçaoRonda)
    A                X                          (1 + 3)
    B                Y                          (2 + 3)
    C                Z                          (3 + 3)

"""

#Organizando num dicionário os valores acima tabelados
jogada = {
    'A' : {'X': 4, 'Y': 8, 'Z': 3},
    'B' : {'X': 1, 'Y': 5, 'Z': 9},
    'C' : {'X': 7, 'Y': 2, 'Z': 6}
}


f = open('input.txt','r')
listaTuplos = []
for linha in f: 
    #obter primeira letra e colocar na primeira posição do tuplo e a segunda letra na segunda posição do mesmo  
    listaTuplos.append(linha.split())
#print(listaTuplos)

total = 0
for l in listaTuplos:
    total += jogada[l[0]][l[1]]
print("\nPontuação Total do Jogo Pedra/Papel/Tesoura foi de {} pontos".format(total)) 