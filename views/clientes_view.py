import tkinter as tk
from tkinter import messagebox

class TelaCadastroCliente:
    def _init_(self, cliente_controller, root):
        self.cliente_controller = cliente_controller
        self.root = root
        self.frame = tk.Frame(self.root)

        self.root.configure(bg="#38618F")
        
        self.root.title("Cadastro de Cliente")

        self.nome_label = tk.Label(self.frame, text="Nome", fg="white")
        self.nome_label.pack(pady=5)
        self.nome_entry = tk.Entry(self.frame, width=30)
        self.nome_entry.pack(pady=5)

        self.email_label = tk.Label(self.frame, text="E-mail", fg="white")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.frame, width=30)
        self.email_entry.pack(pady=5)

        self.telefone_label = tk.Label(self.frame, text="Telefone",  fg="white")
        self.telefone_label.pack(pady=5)
        self.telefone_entry = tk.Entry(self.frame, width=30)
        self.telefone_entry.pack(pady=5)

        self.data_nascimento_label = tk.Label(self.frame, text="Data de Nascimento",  fg="white")
        self.data_nascimento_label.pack(pady=5)
        self.data_nascimento_entry = tk.Entry(self.frame, width=30)
        self.data_nascimento_entry.pack(pady=5)

        self.cadastrar_button = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar_cliente)
        self.cadastrar_button.pack(pady=10)

        self.voltar_button = tk.Button(self.frame, text="Voltar", command=self.voltar)
        self.voltar_button.pack(pady=10)

        self.frame.pack(padx=20, pady=20)

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        data_nascimento = self.data_nascimento_entry.get()

        if nome and email and telefone and data_nascimento:
            if self.cliente_controller.validar_email(email):
                cliente = self.cliente_controller.cadastrar_cliente(nome, email, telefone, data_nascimento)
                messagebox.showinfo("Sucesso", f"Cliente {cliente.nome} cadastrado com sucesso!")
                self.voltar()
            else:
                messagebox.showerror("Erro", "E-mail inválido.")
        else:
            messagebox.showwarning("Campo vazio", "Por favor, preencha todos os campos!")

    def voltar(self):
        self.frame.destroy()
        self.root.deiconify()