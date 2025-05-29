# e-commerce com listas

produtos = ['','iphone 17', 'Notebook dell','fone','SSD']
valores = ['',7000.0,10000.0,400.0,350.55]

print('escolha o produto através do ID 1 - 2 - 3 - 4')
print('PRODUTOS DA LOJA X')
print()
print(produtos[1],' -R$', valores[1])
print(produtos[2],' -R$', valores[2])
print(produtos[3],' -R$', valores[3])
print(produtos[4],' -R$', valores[4])
print()
pedido1 = int(input('Digite o ID do produto'))
pedido2 = int(input('Digite o ID do produto'))
pedido3 = int(input('Digite o ID do produto'))


carrinho = []
meu_total = []


carrinho.append(produtos[pedido1])
carrinho.append(produtos[pedido2])
carrinho.append(produtos[pedido3])

meu_total.append(valores[pedido1])
meu_total.append(valores[pedido2])
meu_total.append(valores[pedido3])

print('PRODUTOS NO CARRINHO - ', carrinho)
total = sum(meu_total)
print('R$', total)

print('Escolha a forma de pagamento 1 pix 2 CC 3 Paypall')
formas = ['','pix', 'CC', 'PayPall']
escolha = int(input('Digite o ID: '))
print('A sua forma de pagamento é ', formas[escolha])
print('----------x--------------')
print('Obrigada Volte Sempre!')