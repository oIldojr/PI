import tkinter as tk
from controllers.acoes_controller import AcoesController

def main():
    root = tk.Tk()
    
    root.withdraw()
    root.after(100, lambda: root.deiconify())
    
    controller = AcoesController(root)
    controller.iniciar_tela()
    
    root.mainloop()

if __name__ == "__main__":
    main()