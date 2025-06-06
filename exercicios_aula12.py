#1-Crie um número aleatório de 5,10

import random

def aleatorio():

  aleatorio =  random.randint(5,10)
  print(aleatorio)

aleatorio()

#2-Crie 3 números aleatórios

import random

def aleatorio():

  aleatorio =  random.randint(0,1000)
  print(aleatorio)

aleatorio()

import random

def aleatorio():

  aleatorio =  random.randint(0,1000)
  print(aleatorio)

aleatorio()

import random

def aleatorio():

  aleatorio =  random.randint(0,1000)
  print(aleatorio)

aleatorio()

#3- Crie um número aleatório entre 10 a 30 utilize o range()

import random

def aleatorio():

  aleatorio =  random.randrange(10,30)
  print(aleatorio)
  
aleatorio()


#4 - Contagem regressiva simples

for variavel in range(10,0,-1):
    print(variavel)
print('Fogo!!!')


#5 - Soma de números pares

n = int(input('Numero:  '))
soma = 0
l =  []
for i in  range(n):
    l.append(i)
    soma =  sum(l)
    print(soma)
    
#6 - Tabuada de multiplicação
    
n = int(input('Digite o multiplicador da tabela: '))
for i in range(0,100):
    
    calculo = i * n
    print( n, 'X', i, '=', calculo)
    
    
#7 - Números ímpares reversos
    
for variavel in range(99,0,-2):
    print(variavel)
print('Fogo!!!')
