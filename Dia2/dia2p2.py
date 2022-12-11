"""
1 -> Pedra [A ou X] 
2 -> Papel [B ou Y]
3 -> Tesoura [C ou Z]


Agora as pomtuaçoes sofrem uma pequena alteração

X siginifica que tenho de perder
Y siginifica que tenho de empatar
Z siginifica que tenho de ganhar

Casos em que tenho de Perder:
Adversario          Eu          Pontuação (jogadaFeita + PontuaçaoRonda)
    A                X                          (3 + 0)
    B                X                          (1 + 0)
    C                X                          (2 + 0)

Casos em que tenho de Vencer:
Adversario          Eu          Pontuação (jogadaFeita + PontuaçaoRonda)
    A                Z                          (2 + 6)
    B                Z                          (3 + 6)
    C                Z                          (1 + 6)


Casos em que tenho de Empatar:
Adversario          Eu          Pontuação (jogadaFeita + PontuaçaoRonda)
    A                Y                          (1 + 3)
    B                Y                          (2 + 3)
    C                Y                          (3 + 3)

"""

#Organizando num dicionário os valores acima tabelados
jogada = {
    'A' : {'X': 3, 'Y': 4, 'Z': 8},
    'B' : {'X': 1, 'Y': 5, 'Z': 9},
    'C' : {'X': 2, 'Y': 6, 'Z': 7}
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