import tkinter as tk

class TelaAcoes:
    def __init__(self,controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root, bg="#38618F")

        self.root.option_add("*Font",("Times New Romam",14,"bold"))
        self.root.configure(bg="#38618F")
        self.root.attributes('-fullscreen',True)
        

    def mostrar(self):
        self.root.title("ClinControl")
        self.frame.pack(padx=20,pady=20)

        tk.Button(self.frame, text="Cadastrar Cliente",width=60,command=self.controller.abrir_cadastro_cliente,bg="#C2E6FF").pack(pady=30)
        tk.Button(self.frame, text="Cadastrar Médico",width=60,command=self.controller.abrir_cadastro_medico,bg="#C2E6FF").pack(pady=30)
        tk.Button(self.frame, text="Calcular IMC",width=60,command=self.controller.abrir_calcula_imc,bg="#C2E6FF").pack(pady=30)
        tk.Button(self.frame, text="Medir Pressão",width=60,command=self.controller.abrir_medir_pressao,bg="#C2E6FF").pack(pady=30)
        tk.Button(self.frame, text="Medir Hemoglobina",width=60,command=self.controller.abrir_medir_hemoglobina,bg="#C2E6FF").pack(pady=30)
        tk.Button(self.frame, text="Vizualizar DashBoard",width=60,command=self.controller.abrir_dashboard,bg="#C2E6FF").pack(pady=30)
        tk.Button(self.frame, text="Sair",width=60,command=self.root.quit,bg="#A8DDf1").pack(pady=30)