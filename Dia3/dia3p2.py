f = open('input.txt','r')
lista = []
for linha in f:    
    lista.append(linha)
#print(lista)

soma = 0
l = 0
while(l <len(lista)):
    #ver o que tem em comum l com l+1 e l+2 e após isso acrescentar a soma e incrementar l para 
    w1 = set(lista[l])
    w2 = set(lista[l+1])
    w3 = set(lista[l+2])
    lst = list(w1 & w2 & w3)
    if '\n' in lst: lst.remove('\n')
    print("Letras em comum nas palavras analisadas: {}".format(lst))
    if(lst[0].islower()): 
        soma += ord(lst[0]) - 96
    else:
        soma += ord(lst[0]) - 38
    l += 3
print("\nA soma total das letras em comum das substrings observadas é: {}".format(soma))