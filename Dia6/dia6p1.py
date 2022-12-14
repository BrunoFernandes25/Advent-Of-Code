#ler linha codigo e a cada 4 caracteres averigua se são todos diferentes, caso sejam soma se o contador 
# e obtem se o total de caracteres necessarios ate se obter os tais 4 diferentes entre todos
f = open("input.txt", "r")
linha = f.readline()
#print(linha)
#print(len(linha))

i=0
while i < len(linha) :
    #verificar se são 4 caracteres diferentes
    if len(set(linha[i:i+4])) == len(linha[i:i+4]):
        caracteres = print('\nSerão precisos {} caracteres até obter uma sequência de 4 caracteres diferentes'.format(i+4))
        break
    i+=1