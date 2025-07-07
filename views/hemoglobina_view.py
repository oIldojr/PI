import tkinter as tk
from tkinter import messagebox

class TelaHemoglobina:
    def __init__(self, parent=None, controller=None):
        self.root = tk.Toplevel(parent) if parent else tk.Tk()
        self.frame = tk.Frame(self.root)
        self.controller = controller

        # Guardar referência à janela principal (master)
        self.master = parent  
        self.hemoglobina_var = tk.StringVar()  

    def mostrar(self):
        if self.master:
            self.master.withdraw()

        self.root.title("Mede Hemoglobina")
        self.root.attributes('-fullscreen', True)  
        self.frame.pack(padx=20, pady=20)  

        # Adicionando os componentes da tela
        tk.Label(self.frame, text="Hemoglobina: ").pack()
        tk.Entry(self.frame, textvariable=self.hemoglobina_var).pack(pady=20)

        tk.Button(self.frame, text="Medir Hemoglobina", command=self.medir_hemoglobina).pack(pady=10)

        tk.Button(self.frame, text="Sair", command=self._sair).pack(pady=10)

    def medir_hemoglobina(self):
        try:
            hemoglobina = float(self.hemoglobina_var.get())
            
            if hemoglobina >= 12.5 and hemoglobina <= 15.5:
                messagebox.showinfo("Resultado", "Os níveis estão normais para um Homem ou uma Mulher.")
            elif hemoglobina < 12.5:
                messagebox.showinfo("Resultado", "Os níveis estão normais para uma criança.")
            else:
                messagebox.showwarning("Resultado", "Níveis elevados de hemoglobina. Consulte um médico.")

        except ValueError:
            messagebox.showerror("Erro", "Verifique as entradas. A hemoglobina precisa ser um número válido.")

    def _sair(self):
        self.root.quit()

        if self.master:
            self.master.deiconify()