from views.hemoglobina_view import TelaHemoglobina

class HemoglobinaController:
    def __init__(self,root):
          self.root = root
          self.view = TelaHemoglobina(self.root,self)
    
    def iniciar_tela(self):
        self.view_mostrar()
