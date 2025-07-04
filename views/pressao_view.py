import tkinter as tk
from tkinter import messagebox

class TelaPressao:
    def __init__(self, parent=None, controller=None):
        self.root = tk.Toplevel(parent) if parent else tk.Tk()  
        self.frame = tk.Frame(self.root)
        self.controller = controller

        self.pressao_var = tk.StringVar()  
      
    def mostrar(self):
        self.root.title("Mede Pressão")
        self.root.attributes('-fullscreen', True)  
        self.frame.pack(padx=20, pady=20)  

        tk.Label(self.frame, text="Pressão: ").pack()
        tk.Entry(self.frame, textvariable=self.pressao_var).pack(pady=20)

        tk.Button(self.frame, text="Medir Pressão", command=self.medir_pressao).pack(pady=10)

    def medir_pressao(self):
        try:
            pressao = float(self.pressao_var.get())
            
            if pressao < 120.80:
                messagebox.showinfo("Resultado", "A pressão do paciente está normal.")
            elif 120.80 <= pressao < 139.89:
                messagebox.showinfo("Resultado", "O paciente está com Pré-Hipertensão. Atenção!")
            elif 140.90 <= pressao < 159.99:
                messagebox.showinfo("Resultado", "O paciente está com Hipertensão estágio 1.")
            elif pressao >= 160.00:
                messagebox.showinfo("Resultado", "O paciente está com Hipertensão estágio 2.")
        except ValueError:
            messagebox.showerror("Erro", "Verifique as entradas. A pressão precisa ser um número válido.")

    
    def _voltar(self):
        self.root.destroy()
        if hasattr(self, 'master') and self.master:  
            self.master.deiconify()