import tkinter as tk
from tkinter import ttk

class DashboardView:
    def _init_(self, root, controller):
        self.root = tk.Toplevel(root)
        self.root.title("Dashboard - ClinControl")
        self.root.attributes('-fullscreen', True)
        self.controller = controller

        self.frame = ttk.Frame(self.root, padding=50)
        self.frame.pack(expand=True)

    def mostrar(self, dados):
        ttk.Label(self.frame, text="📊 Dashboard de Indicadores", font=("Arial", 20, "bold")).pack(pady=20)

        ttk.Label(self.frame, text=f"Total de Clientes: {dados['clientes']}", font=("Arial", 14)).pack(pady=10)
        ttk.Label(self.frame, text=f"Total de Médicos: {dados['medicos']}", font=("Arial", 14)).pack(pady=10)
        ttk.Label(self.frame, text=f"Total de Agendamentos: {dados['agendamentos']}", font=("Arial", 14)).pack(pady=10)
        ttk.Label(self.frame, text=f"Agendamentos Pendentes: {dados['pendentes']}", font=("Arial", 14)).pack(pady=10)

        ttk.Button(self.frame, text="Sair", command=self.root.destroy).pack(pady=30)