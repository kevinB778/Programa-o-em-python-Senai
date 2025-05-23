# SISTEMA DE MÉDIA DE NOTAS


print('SEJA BEM VINDO(A) AO SISTEMA DE NOTAS')

nome = input('Digite o nome do aluno: ')

nota_mat = float(input('Digite a nota de matemática: '))
nota_por = float(input('Digite a nota de Portugues: '))
nota_ing = float(input('Digite a nota de inglês: '))

media = (nota_mat + nota_por + nota_ing) / 3
    
print('O aluno',nome, ' esta com a media', media)

aprovado  = media >= 7
reprovado  = media < 5
recuperacao  = media >=5 and media < 7

print(f'''

APROVADO - {aprovado}
REPROVADO - {reprovado}
RECUPERAÇÃO - {recuperacao}
''')