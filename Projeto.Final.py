import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def conectar():
    return sqlite3.connect('teste.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
       CREATE TABLE IF NOT EXISTS usuarios(
       nome INTEGER NOT NULL,
       email TEXT NOT NULL,
       telefone TEXT NOT NULL,
       endereco TEXT NOT NULL                    
       ) 
''')
    conn.commit()
    conn.close()


def inserir_usuario():
    nome  = entry_nome.get()
    email = entry_email.get()    
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()
    if nome and email and telefone and endereco:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(nome, email, telefone, endereco)  VALUES(?,?,?,?)',(nome, email, telefone, endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO')

# READ LER            

def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0],usuario[1],usuario[2],usuario[3]))
    conn.close()    


def delete_usuario():
    dados_del  = tree.selection()
    if dados_del:
       user_telefone = tree.item(dados_del)['values'][2]         
       conn = conectar()
       c = conn.cursor()
       c.execute('DELETE FROM usuarios WHERE telefone = ? ' ,(user_telefone,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()
    else:
        messagebox.showerror('ERRO','OCORREU UM ERRO')   
 
        
def editar():
    selecao = tree.selection()
    if selecao:
        user_telefone =  tree.item(selecao)['values'][2]
        novo_nome =  entry_nome.get()
        novo_email = entry_email.get()
        novo_endereco = entry_endereco.get()
        if novo_nome and novo_email and novo_endereco:
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE usuarios SET nome = ?, email = ?, endereco = ? WHERE telefone = ?', (novo_nome, novo_email, novo_endereco, user_telefone))

            conn.commit()
            conn.close()
            messagebox.showinfo('EDIÇÃO', 'DADOS EDITADOS')
            mostrar_usuario()
        else: 
            messagebox.showerror('Erro','NÃO HOUVE ALTERAÇÃO')
    else:
        messagebox.showwarning('', 'PREENCHA TUDO')

janela = tk.Tk()
janela.configure(bg="#178DB1")
janela.title('CRUD')
janela.geometry('1000x1000')

TITULO = tk.Label(janela,text = 'SISTEMA DE CADASTRO DO VAREJO',fg = 'dark blue',  font=('roboto', 20, 'bold'))
TITULO.grid(row=0,column=11,padx=10, pady=10)

#---------------------------------------------------------------------------------
label_nome  = tk.Label(janela, text='NOME: ', font=('arial', 16))
label_nome.grid(row=1,column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela, font=('arial', 16))
entry_nome.grid(row=1,column=1, padx=10, pady=10)
# ---------------------------------------------------------------------------------
label_email  = tk.Label(janela, text='E-MAIL: ', font=('arial', 16))
label_email.grid(row=2,column=0, padx=10, pady=10)

entry_email = tk.Entry(janela, font=('arial', 16))
entry_email.grid(row=2,column=1, padx=10, pady=10)

label_endereco  = tk.Label(janela, text='Endereco: ', font=('arial', 16))
label_endereco.grid(row=5,column=0, padx=10, pady=10)

entry_endereco =  tk.Entry(janela, font=('arial', 16))
entry_endereco.grid(row=5,column=1, padx=10, pady=10)

label_telefone  = tk.Label(janela, text='Telefone: ', font=('arial', 16))
label_telefone.grid(row=3,column=0, padx=10, pady=10)

entry_telefone =  tk.Entry(janela, font=('arial', 16))
entry_telefone.grid(row=3,column=1, padx=10, pady=10)

btn_salvar = tk.Button(janela, text = 'Salvar', font= ('arial', 16), command=inserir_usuario)
btn_salvar.grid(row=12,column=15, padx=2, pady=30) 

btn_editar = tk.Button(janela, text = 'Editar', font= ('arial', 16), command=editar)
btn_editar.grid(row=12,column=13, padx=2, pady=30) 

btn_Deletar = tk.Button(janela, text = 'Deletar', font= ('arial', 16), command=delete_usuario)
btn_Deletar.grid(row=12,column=16, padx=2, pady=30) 


columns = ('NOME', 'E-MAIL','TELEFONE', 'ENDERECO')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=20, column=10, columnspan=2,padx=20, pady=20)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()

janela.mainloop()