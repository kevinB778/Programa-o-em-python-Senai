# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS. 


numero1 = int(input('digite um numero: '))

if numero1 % 2 == 0:
    print('é par')
    
else:
    print('é impar')
    


numero2 = int(input('digite um numero: '))
if numero2 % 2 == 0:
    print('é par')
    
else:
    print('é impar')

def comparar():
    comparar = numero1 == numero2
    print(comparar)
    
comparar()
    
#CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
    
numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))
numero3 = int(input('digite um numero: '))

def multiplicacao():
    multiplicar = numero1 * numero2 * numero3
    print(multiplicar)
    
multiplicacao()

#CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))

def elevado():
    elevado = numero1**numero2
    print(elevado)
    
elevado()


