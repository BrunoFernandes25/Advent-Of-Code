f = open('input.txt','r')
lista = []
for linha in f:    
    lista.append(linha)
lista = [x[:-1] for x in lista]
#print(lista)

#                                      x           y
#                                 x[0] - x[1],y[1] - y[2]
# Dar split nas "," e ver se aqui  71  - 89  ,66   - 70
soma = 0
for l in lista:
    pares = l.split(',')
    x = pares[0].split('-')
    y =pares[1].split('-')
    #print(pares)
    #print('Pares: {}\nX: {},Y: {}\n'.format(pares,x,y))

    #Verificar se algum par está completamente dentro de outro
    if((int(x[0])>=int(y[0]) and int(x[1])<=int(y[1])) or (int(y[0])>=int(x[0]) and int(y[1])<=int(x[1]))):
        soma +=1
print('\nA soma total de grupos contidos completamente noutros é: {}'.format(soma))