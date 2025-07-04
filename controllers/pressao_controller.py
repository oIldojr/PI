from views.pressao_view import TelaPressao

class PressaoController:
    def __init__(self, root):
        self.root = root  
        self.view = TelaPressao(self.root, self) 

    def iniciar_tela(self):
        self.view.mostrar()