# vazia
lista = []

# lista preenchida
lista_teste = [1,2,3,4,5]

#indices
lista_teste[5] = 100
print(lista_teste)

#funções

lista = []

#alteram a estrutura da lista
# append() extend() +=() insert()

# append vai adicionar apenas 1 dado no final da lista -> extend() +=()
lista.extend([10,20,30,40,50,100, 'teste', True ])
print(lista)

lista += ('a', 'b')
print(lista)

# add dado em um indice especifico
lista.insert(0,200)

print(lista)

# deletar dado del remove pop

lista.pop() # deletar o ultimo dado

lista.pop(0) #deletar o indice que vc declarou

print(lista)

lista.remove('a') #remove o valor que vc vê

del list[0] # deleta o indice

print(lista)

print(len(lista))


