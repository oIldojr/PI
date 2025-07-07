import tkinter as tk
from tkinter import messagebox

class TelaIMC:
    def __init__(self, parent=None):
        self.root = tk.Toplevel(parent) if parent else tk.Tk()
        self.frame = tk.Frame(self.root)

        self.peso_var = tk.StringVar()
        self.altura_var = tk.StringVar()
       
        self.mostrar()

    def mostrar(self):
        self.root.title("Calculadora de IMC")
        self.root.attributes('-fullscreen', True)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Peso (kg):").pack()
        tk.Entry(self.frame, textvariable=self.peso_var).pack(pady=20)

        tk.Label(self.frame, text="Altura (m):").pack()
        tk.Entry(self.frame, textvariable=self.altura_var).pack(pady=20)

        tk.Button(self.frame, text="Calcular IMC", command=self.calcular_imc).pack(pady=10)
        tk.Button(self.frame, text="Sair", command=self.root.destroy).pack(pady=30)

    
    def calcular_imc(self):
        try:
            peso = float(self.peso_var.get())
            altura = float(self.altura_var.get())
            if altura <= 0:
                raise ValueError("Altura deve ser maior que zero.")
            imc = peso / (altura ** 2)
            categoria = self.classificar_imc(imc)
            messagebox.showinfo("Resultado", f"Seu imc é: {imc:.2f} ({categoria})")
        except ValueError as e:
            messagebox.showerror("Erro", f"Verifique as entradass: {e}")

    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"
        
    def _voltar(self):
        self.root.destroy()
        if hasattr(self, 'master') and self.master:  # Se houver uma janela principal
            self.master.deiconify()  # Mostra a janela principal novamente