import tkinter as tk
from tkinter import ttk

class TelaAcoes:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = None
        self._configurar_estilos()
        
    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#38618F')
        self.style.configure('Botao.TButton', background='#C2E6FF', 
                           font=('Times New Roman', 14, 'bold'))
        self.style.configure('BotaoSair.TButton', background='#A8DDF1')

    def mostrar(self):
        self._configurar_janela()
        self._criar_botoes()
        
    def _configurar_janela(self):
        self.root.title("ClinControl - Menu Principal")
        self.root.configure(bg='#38618F')
        self.root.attributes('-fullscreen', True)
        
        # Centralizar conteúdo
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def _criar_botoes(self):
        if self.frame:
            self.frame.destroy()
            
        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=0, column=0, sticky='nsew', padx=100, pady=50)
        
        botoes = [
            ("Cadastrar Cliente", self.controller.abrir_cadastro_cliente),
            ("Cadastrar Médico", self.controller.abrir_cadastro_medico),
            ("Calcular IMC", self.controller.abrir_calcula_imc),
            ("Medir Pressão", self.controller.abrir_medir_pressao),
            ("Medir Hemoglobina", self.controller.abrir_medir_hemoglobina),
            ("Visualizar Dashboard", self.controller.abrir_dashboard)
        ]
        
        for texto, comando in botoes:
            btn = ttk.Button(
                self.frame,
                text=texto,
                style='Botao.TButton',
                command=comando,
                width=40
            )
            btn.pack(pady=15, ipady=10)
        
        ttk.Button(
            self.frame,
            text="Sair",
            style='BotaoSair.TButton',
            command=self.root.quit,
            width=40
        ).pack(pady=15, ipady=10)