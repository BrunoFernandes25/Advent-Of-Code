#encontrar o top3 elfos mais calóricos
#colocar cada soma calorica de cada elfo numa lista e ordenar a lista por ordem crescente

f = open('input.txt','r')
lista = []
for linha in f:    
    lista.append(linha)
#print(lista)


soma = 0
top3 = []

for l in lista:
    if l == "\n":
    #verificar se "soma > somaMax" e caso seja,atribui-se os novos valores a somaMax e damos reset a variavel soma
        top3.append(soma)
        soma = 0
    else:
        soma += int(l)

#ordenar lista decrescente
top3.sort(reverse= True)
print(top3[0] + top3[1] + top3[2])  
print("\nOs elfos mais calóricos contêm : \n1-> {} calorias \n2-> {} calorias \n3-> {} calorias".format(top3[0],top3[1],top3[2]))  