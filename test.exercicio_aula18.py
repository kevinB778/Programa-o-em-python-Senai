import tkinter as tk



def display():
    nome = nome_digitado.get()
    idade = idade_digitada.get()
    email = email_digitado.get()
    endereco = endereco_digitado.get()
    celular = celular_digitado.get()

    MOSTRAR_NOME.config(text=nome)
    MOSTRAR_IDADE.config(text=idade)
    MOSTRAR_EMAIL.config(text=email)
    MOSTRAR_ENDERECO.config(text=endereco)
    MOSTRAR_CELULAR.config(text=celular)
    


janela  =  tk.Tk()
janela.title('SISTEMA DE CADASTRO ')

janela.geometry('500x500')

titulo_pag = tk.Label(janela,text = 'Cadastro de usuários', font=('arial',20))
titulo_pag.grid(row=0,column=0, padx=15, pady=10)


nome_ =  tk.Label(janela, text = 'NOME', bg='yellow', font=('arial',10))
nome_.grid(row=1, column=0, pady=5)

nome_digitado =  tk.Entry(janela, font=('arial', 10))
nome_digitado.grid(row=1, column=1, padx=5, pady=5)


texto =  tk.Label(janela, text = 'IDADE', bg='yellow', font=('arial',10))
texto.grid(row=2, column=0, pady=5)

idade_digitada =  tk.Entry(janela, font=('arial', 10))
idade_digitada.grid(row=2, column=1, padx=5, pady=5)

celular_ =  tk.Label(janela, text = 'CELULAR', bg='yellow', font=('arial',10))
celular_.grid(row=3, column=0, pady=5)

celular_digitado =  tk.Entry(janela, font=('arial', 10))
celular_digitado.grid(row=3, column=1, padx=5, pady=5)

email_ =  tk.Label(janela, text = 'EMAIL', bg='yellow', font=('arial',10))
email_.grid(row=4, column=0, pady=5)

email_digitado =  tk.Entry(janela, font=('arial', 10))
email_digitado.grid(row=4, column=1, padx=5, pady=5)

endereco_ =  tk.Label(janela, text = 'ENDERECO', bg='yellow', font=('arial',10))
endereco_.grid(row=6, column=0, pady=5)

endereco_digitado =  tk.Entry(janela, font=('arial', 10))
endereco_digitado.grid(row=6, column=1, padx=5, pady=5)





b_t = tk.Button(janela, text = 'clique aqui', font=('arial', 15), command=display)
b_t.grid(row=10, column=1, padx=5, pady=5)



ESPACO = tk.Label(janela, text = ' ',  font=('arial', 15))
ESPACO.grid(row=7, column=0, padx=5, pady=5)

MOSTRAR_NOME = tk.Label(janela, text = ' MOSTRAR NOME',  font=('arial', 15))
MOSTRAR_NOME.grid(row=8, column=0, padx=5, pady=5)


MOSTRAR_IDADE = tk.Label(janela, text = 'MOSTRAR IDADE', font=('arial', 15))
MOSTRAR_IDADE.grid(row=9, column=0, padx=5, pady=5)

MOSTRAR_CELULAR = tk.Label(janela, text = ' MOSTRAR CELULAR',  font=('arial', 15))
MOSTRAR_CELULAR.grid(row=10, column=0, padx=5, pady=5)

MOSTRAR_EMAIL = tk.Label(janela, text = ' MOSTRAR EMAIL',  font=('arial', 15))
MOSTRAR_EMAIL.grid(row=11, column=0, padx=5, pady=5)

MOSTRAR_ENDERECO = tk.Label(janela, text = ' MOSTRAR ENDERECO',  font=('arial', 15))
MOSTRAR_ENDERECO.grid(row=12, column=0, padx=5, pady=5)






janela.mainloop()