#3 Verificando se uma string é vazia ou não

s = ''

match s:
    case '':
        print('Vazio')
    case _:
        print('Não é vazio')

# 4 - Verificando se um número é maior, menor ou igual a 10

numero = int(input('Digite um numero: '))

match numero:
    case x if x == 10:
        print('é igual a 10')
    case x if x > 10:
        print('numero é maior que 10')
    case x if x < 10:
        print('numero é menor que 10')

# 5 - Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)

idade = int(input('Digite sua idade'))

match idade:
    case x if x <=12:
        print('é criança')
    case x if x >12 and x <= 17:
        print('é adolecente')
    case x if x >17 and x <= 35:
        print('é jovem')
    case x if x >35 and x <= 64:
        print('é adulto')
    case x if x <= 65:
        print('é idoso')