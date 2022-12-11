f = open('input.txt','r')
lista = []
for linha in f:    
    lista.append(linha)
#print(lista)


"""
A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters 
represent items in the first compartment, while the second half of the characters represent items in the second compartment.

vJrwpWtwJgWrhcsFMMfFFhFp (tamannho:24)           1º -> vJrwpWtwJgWr (12) 2º-> hcsFMMfFFhFp (12)
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL (tamanho:32)    1º -> jqHRNqRjqzjGDLGL (16) 2º-> rsFMfFZSrLrFZsSL (16)
PmmdzqPrVvPwwTWBwg                                  .................................
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn                      .................................
ttgJtRGJQctTZtZT                                    .................................
CrZsJsPPZsGzwwsLwLmpwMDw                            .................................


    Prioridades:
     - Lowercase item types a through z have priorities 1 through 26.
     - Uppercase item types A through Z have priorities 27 through 52.


"""
#i = 0
soma = 0
for l in lista:
    #saber tamanho da lista e dividir em 2 partes
    # apos isto ver o que tem em comum essas duas palavras novas e atribuir as respetivas prioridades
    #No fim somar as prioridades
    w1 = l[0:len(l)//2]
    w2 = l[-len(l)//2:-1]
    x = ''.join(set(w1).intersection(w2))
    #print("Linha {} -> Palavra {} letra em comum {}".format(i,l,x))
    #i +=1
    # a-z
    # a em ASCII tem valor 97 logo como queremos que tenha valor 1
    if(x.islower()):
        soma += ord(x) - 96
    #A-Z
    # A em ASCII tem valor 65 logo como queremos que tenha valor 27
    else:
        soma += ord(x) - 38

print("\nA soma total das letras em comum das substrings observadas é: {}".format(soma))
