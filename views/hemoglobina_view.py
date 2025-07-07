import tkinter as tk
from tkinter import messagebox

class TelaHemoglobina:
    def __init__(self, parent=None, controller=None):
        self.root = tk.Toplevel(parent) if parent else tk.Tk()  
        self.frame = tk.Frame(self.root)
        self.controller = controller

        self.hemoglobina_var = tk.StringVar()  
      
    def mostrar(self):
        self.root.title("Mede Hemoglobina")
        self.root.attributes('-fullscreen', True)  
        self.frame.pack(padx=20, pady=20)  

        tk.Label(self.frame, text="Hemoglobina: ").pack()
        tk.Entry(self.frame, textvariable=self.hemoglobina_var).pack(pady=20)

        tk.Button(self.frame, text="Medir Hemglobina", command=self.medir_hemoglobina).pack(pady=10)

    def medir_hemoglobina(self):
        try:
            hemoglobina = float(self.hemoglobina_var.get())
            
            if hemoglobina >= 12.5 and hemoglobina <= 15.5:
                messagebox.showinfo("Resultado","Os níveis então normais para um Homem ou uma Mulher")
            elif hemoglobina < 12.5:
                messagebox.showinfo("Resultado", "Os niveis estão normais para uma criança")
                
        except ValueError:
            messagebox.showerror("Erro", "Verifique as entradas. A pressão precisa ser um número válido.")

    
    def _voltar(self):
        self.root.destroy()
        if hasattr(self, 'master') and self.master:  
            self.master.deiconify()