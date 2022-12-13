import re
import numpy as np

f = open('input.txt','r')
lista = []
for linha in f:    
    lista.append(linha)
#lista = [x[:-1] for x in lista]
#print(lista)
# regex que encontra ( {4}|[A-Z]) ' '(espaço) 4vezes que indica que nao tem caracter nessa posiçao, ou entao encontra uma letra

stack_Input = [] #cada pedaço de stack encontrada
lista_Stacks = [] #lista com as stacks todas
stacks = []
for l in lista[:8]:
    stack_Input = re.findall('( {4}|[A-Z])', l)
    if(stack_Input != []):
        #print(stack_Input)
        lista_Stacks.append(stack_Input)
#print(lista_Stacks)

#obter as stacks como elas são
listas_Transpostas = np.array(lista_Stacks).T.tolist()
#print(listas_Transpostas)

#colocar a stack da maneira correta, ou seja, ultimo elemento a ser inserido está no topo da lista, isto é, ultimo elem que aparece na lista
count = 1
for i in listas_Transpostas:
    i.reverse()
    stacks.append(i)
    #print('Stack {} -> {}'.format(count,i))
    count += 1
#print(stacks)


#remover espaços
ss = []
cs = 1
for list in stacks:
    a = ' '.join(list).split()
    ss.append(a)
    print('Stack {} -> {}'.format(cs,a))    #stacks sem os '' como elementos na sua composição
    cs += 1
#print(ss)

#ler linhas dos movimentos e realizar tais movimentos até ao final e descobrir quais os elems no topo de cada stack
#print(lista[10:])
c = 1
for l in lista[10:]:
    num = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)",l)
    #print(num)
    
    quant = int(num.group(1))
    origem = int(num.group(2))
    destino = int(num.group(3))
    #print('Movimento {} Origem {} stack correspondente {}'.format(c,origem,ss[origem-1]))
    #c+=1
    #print('Movimento {} Destino {} stack correspondente {}'.format(c,destino,ss[destino-1]))
    #c+=1
    #print('Movimento {} Quantidade {}'.format(c,quant))    
    #c+=1


    #Atribuir os Movimento
    #remover x elems(quant) da origem e atribui pela mesma ordem que se retira, coloca los no destino
 
    #print('\nMovimento {}'.format(c))
    #print('Origem {}'.format(origem))
    #print('Destino {}'.format(destino))
    #print('Quantidade {}'.format(quant))
    #print(ss[origem-1])
    #print('\n\n')

    i=1
    while i <= quant:
        if ss[origem-1] != []:
            #remover elem da lista origem
            l = ss[origem-1].pop()

            #adicionar na lista destino
            ss[destino-1].append(l)
        i+=1
    #c+=1

#Print a StacK Final após todos os movimentos
print()
c1 = 1
for list in ss:
    print('Stack {} -> {}'.format(c1,ss[c1-1]))
    c1 += 1

#TDCHVHJTG