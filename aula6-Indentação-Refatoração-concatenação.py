# indentação em python - organizar o código py
# tipo de organização do código
# variável precisa estar dentro da borda
# quando estiver dentro de nenhum espaço
# quando estiver dentro de um escopo
# precisa ter pelo menos um espaço
# o padrão são 4 espaços
variavel = 'teste'

if variavel == 'teste':
   print('ok')

for n in range(1,10):
   print(n)

else:
   print('teste2')

if 1 > 10:
    x= 10

# Concatenação

nome = 'Maria'
print('Olá, seja bem vinda', nome)
print('Olá, seja bem vinda' +' '+ nome)
print('Olá, seja bem vinda {}'.format(nome))
print('Olá, seja bem vinda %s'%(nome))
print('Olá, seja bem vinda {nome}')
print('Olá, seja bem vinda\n', nome)
# Refatorar = melhorar o código

nome = 'Julio'
sobrenome = 'Cesar'

print('Hello', nome, sobrenome)


