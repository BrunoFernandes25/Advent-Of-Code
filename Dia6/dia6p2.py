f = open("input.txt", "r")
linha = f.readline()
#print(linha)
#print(len(linha))

i=0
while i < len(linha) :
    #verificar se são 14 caracteres diferentes
    if len(set(linha[i:i+14])) == len(linha[i:i+14]):
        caracteres = print('\nSerão precisos {} caracteres até obter uma sequência de 4 caracteres diferentes'.format(i+14))
        break
    i+=1