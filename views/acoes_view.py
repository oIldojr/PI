import tkinter as tk

class TelaAcoes:
    def __init__(self,controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root)
        

    def mostrar(self):
        self.root.title("ClinControl")
        self.frame.pack(padx=20,pady=20)

        tk.Button(self.frame, text="Cadastrar Cliente",width=30,command=self.controller.abrir_cadastro_cliente)
        tk.Button(self.frame, text="Cadastrar Médico",width=30,command=self.controller.abrir_cadastro_medico)
        tk.Button(self.frame, text="Calcular IMC",width=30,command=self.controller.abrir_calcula_imc)
        tk.Button(self.frame, text="Medir Pressão",width=30,command=self.controller.abrir_medir_pressao)
        tk.Button(self.frame, text="Medir Hemoglobina",width=30,command=self.controller.abrir_medir_hemoglobina)
        tk.Button(self.frame, text="Vizualizar DashBoard",width=30,command=self.controller.abrir_dashboard)