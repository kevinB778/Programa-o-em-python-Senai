banco_dados =  {}

nome1 = input('Nome')
idade1 = input('Idade')
senha1 = input('Senha')

nome2 = input('Nome')
idade2 = input('Idade')
senha2 = input('Senha')

nome3 = input('Nome')
idade3 = input('Idade')
senha3 = input('Senha')

banco_dados['nomes'] = [nome1, nome2, nome3]
banco_dados['idades'] = [idade1, idade2, idade3]
banco_dados['senhas'] = [senha1, senha2, senha3]

print(banco_dados)


# ACESSO:

login_nome = input('Digite seu nome >>')
senha_acesso = input('Digite sua senha >> ')


if login_nome in banco_dados['nomes'] and senha_acesso in banco_dados['senhas']:
    print('Seja bem vindo ao sistema!')
else:
    print('Acesso negado, tente novamente!')





























