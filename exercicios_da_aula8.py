# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.

numero = int(input('digite um numero: '))
if numero > 0:
    print('é positivo')
if numero < 0:
    print('é negativo')
if numero == 0:
	print('é zero')


# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade =  int(input('Digite sua idade'))
titulo_eleitor  =  input('Possui Título de eleitor? s ou n')

if idade >= 16 and titulo_eleitor == 's':
    print('Pode votar')
else:
    print('Você não pode Votar')
    
    
# 3*
# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

numero = int(input('digite um numero'))
if numero % 2 == 0:
    print('o numero é par')
else:
	print('o numero é impar')
	
	
# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

l1 = 1
l2 = 2
l3 = 3

if l1 == l2 == l3 == l1:
    print('Equilatero')
elif l1 != l2 != l3 != l1:
    print('Escaleno')
else: 
    print('isocesles')  

# 5*
# Determine se um número é múltiplo de 5 e 7.

multiplo  = int(input('nº>  '))

if multiplo % 5 == 0 and multiplo % 7 == 0:
    print('São multiplos')
elif multiplo % 5 == 0 or multiplo % 7 == 0:
    print('Apenas 1 é multiplo')
else:
    print('nenhum é...')


# 6*
# Verifique se um número é positivo e maior que 10

numero = int(input('digite um numero: '))
if numero > 10:
    print('é positivo')
if numero <= 10:
	print('é negativo')

# 7*

# Verifique se um número é divisível por 3 ou 5.
    
n1   =  15

if n1 % 3 == 0 and n1 % 5==0:
    print('São divisiveis')
else:
    print('Não são!')