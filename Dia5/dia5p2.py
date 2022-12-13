import re
import numpy as np

f = open('input.txt','r')
lista = []
for linha in f:    
    lista.append(linha)

stack_Input = [] #cada pedaço/linha de input de stack encontrada
lista_Stacks = [] #lista com as stacks todas(que são listas também)
for l in lista[:8]:
    stack_Input = re.findall('( {4}|[A-Z])', l)
    if(stack_Input != []):
        #print(stack_Input)
        lista_Stacks.append(stack_Input)
#print(lista_Stacks)

stacks = []
listas_Transpostas = np.array(lista_Stacks).T.tolist()
#print(listas_Transpostas)
count = 1
for i in listas_Transpostas:
    i.reverse()
    stacks.append(i)
    #print('Stack {} -> {}'.format(count,i))
    count += 1
#print(stacks)

ss = []
cs = 1
for list in stacks:
    a = ' '.join(list).split()
    ss.append(a)
    print('Stack {} -> {}'.format(cs,a))    #stacks sem os '' como elementos na sua composição
    cs += 1
#print(ss)

c = 1
mov=1
for l in lista[10:]:
    num = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)",l)
    
    quant = int(num.group(1))
    origem = int(num.group(2))
    destino = int(num.group(3))

    if quant == 1:
       if ss[origem-1] != []:
            #remover elem da lista origem
            l = ss[origem-1].pop()
            #adicionar na lista destino
            ss[destino-1].append(l) 
    else:
        temp = []
        i=1
        while i <= quant:
            if ss[origem-1] != []:
                #remover elem da lista origem
                l = ss[origem-1].pop()
                #adicionar na lista temporaria
                temp.append(l)
            i += 1
        temp.reverse()
        #print(temp)
        for i in temp:
            ss[destino-1].append(i)
    mov +=1

print()
c1 = 1
for list in ss:
    print('Stack {} -> {}'.format(c1,ss[c1-1]))
    c1 += 1
#NGCMPJLHV