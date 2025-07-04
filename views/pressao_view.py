import tkinter as tk
from tkinter import messagebox

class TelaPressao:
    def __init__(self, parent=None):
        self.root = tk.Toplevel(parent) if parent else tk.Tk()
        self.frame = tk.Frame(self.root)

        self.pressao_var = tk.StringVar()
      
        self.mostrar()

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
                 messagebox.showinfo("A pressão do paciente está´normal)")

            elif pressao > 120.80 and pressao < 139.89:
                 messagebox.showinfo("O paciente está com Pré-Hipertensão,atenção)")

            elif pressao > 140.90 and pressao < 159.99:
                messagebox.showinfo("O paciente está com Hipertensão estágio 1)")

            elif pressao > 160.100:
                messagebox.showinfo("O paciente está com Hipertensão estágio 2)")

        except ValueError as e:
            messagebox.showerror("Erro", f"Verifique as entradass: {e}")

    def _voltar(self):
        self.root.destroy()
        if hasattr(self, 'master') and self.master:  # Se houver uma janela principal
            self.master.deiconify()  # Mostra a janela principal novamente


    