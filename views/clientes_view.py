import tkinter as tk
from tkinter import messagebox, ttk

class TelaCadastroCliente:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = None
        self._configurar_estilos()
        
    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#38618F')
        self.style.configure('TLabel', background='#38618F', foreground='white', 
                           font=('Times New Roman', 14, 'bold'))
        self.style.configure('TEntry', font=('Times New Roman', 12))
        self.style.configure('Botao.TButton', background='#C2E6FF')
        self.style.configure('BotaoVoltar.TButton', background='#A8DDF1')

    def mostrar(self):
        self._configurar_janela()
        self._criar_formulario()
        
    def _configurar_janela(self):
        self.root.title("Cadastro de Cliente")
        self.root.configure(bg='#38618F')
        self.root.attributes('-fullscreen', True)
        
        # Centralizar conteúdo
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def _criar_formulario(self):
        if self.frame:
            self.frame.destroy()
        
        # Frame principal que centraliza
        self.frame = ttk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Frame do formulário
        form_frame = ttk.Frame(self.frame, padding=20, style='Form.TFrame')
        form_frame.pack()
        
        # Configurar estilo do frame do formulário
        self.style.configure('Form.TFrame', background='#38618F', borderwidth=2, relief='groove')
        
        # Campos do formulário
        campos = [
            ("Nome:", 'nome'),
            ("E-mail:", 'email'), 
            ("Telefone:", 'telefone'),
            ("Data Nascimento (DD/MM/AAAA):", 'data_nascimento')
        ]
        
        self.entries = {}
        
        for i, (label, nome_campo) in enumerate(campos):
            ttk.Label(form_frame, text=label).grid(row=i, column=0, pady=10, sticky='e')
            entry = ttk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, pady=10, padx=10, sticky='w')
            self.entries[nome_campo] = entry
        
        # Frame dos botões
        botoes_frame = ttk.Frame(form_frame)
        botoes_frame.grid(row=len(campos)+1, column=0, columnspan=2, pady=20)
        
        ttk.Button(botoes_frame, text="Cadastrar", 
                style='Botao.TButton',
                command=self._cadastrar).pack(side=tk.LEFT, padx=10)
                
        ttk.Button(botoes_frame, text="Voltar",
                style='BotaoVoltar.TButton',
                command=self._voltar).pack(side=tk.LEFT, padx=10)
    
    def _cadastrar(self):
        try:
            dados = {
                'nome': self.entries['nome'].get(),
                'email': self.entries['email'].get(),
                'telefone': self.entries['telefone'].get(),
                'data_nascimento': self.entries['data_nascimento'].get()
            }
            
            if any(not valor for valor in dados.values()):
                raise ValueError("Todos os campos são obrigatórios")
                
            cliente = self.controller.cadastrar_cliente(**dados)
            messagebox.showinfo("Sucesso", f"Cliente {cliente.nome} cadastrado!")
            self._limpar_campos()  
            
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def _limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
    
    def _voltar(self):
        self.root.destroy()
        if hasattr(self, 'master') and self.master:  # Se houver uma janela principal
            self.master.deiconify()  # Mostra a janela principal novamente