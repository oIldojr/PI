from controllers.acoes_controller import AcoesController
import tkinter as tk

def main():
    root = tk.Tk()
    controller = AcoesController(root)
    controller.iniciar_tela()
    root.mainloop()
    
    
if __name__ == "__main__":
    main()