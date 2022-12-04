f = open('input.txt','r')
count = 0
lista = []
for linha in f:    
    count +=1
    lista.append(linha)
#print(lista)

# para cada linha, enquanto tivermos números somamos e atribuimos o valor à variavel soma e atualizamos somaMax conforme seja encontrado '\n' na lista
somaMax = 0
soma = 0

for l in lista:
    if l == "\n":
    #verificar se "soma > somaMax" e caso seja,atribui-se os novos valores a somaMax e damos reset a variavel soma
        if soma > somaMax:
            somaMax = soma
        soma = 0
    else:
        soma += int(l)

print("\nA soma do elfo mais calórico é {}".format(somaMax))  