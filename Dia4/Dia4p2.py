f = open('input.txt','r')
lista = []
for linha in f:    
    lista.append(linha)
lista = [x[:-1] for x in lista]
#print(lista)

#overlaps é quando temos 2-8 e 3-7, ocorre overlap entre o 3 e o 7(comum em ambos)
soma = 0
for l in lista:
    pares = l.split(',')
    x = pares[0].split('-')
    y =pares[1].split('-')
    #print(pares)
    #print('Pares: {}\nX: {},Y: {}\n'.format(pares,x,y))

    #Verificar se algum par está completamente dentro de outro
    if(int(y[1])>=int(x[0]) and int(y[1])<=int(x[1]) or 
        int(x[1])>=int(y[0]) and int(x[1])<=int(y[1]) or
        int(x[0])>=int(y[0]) and int(x[0])<=int(y[1]) or
        int(y[1])>=int(x[0]) and int(y[1])<=int(x[1])):
        soma += 1
print('\nA soma total de intervalos sobrepostos é: {}'.format(soma)) #867
