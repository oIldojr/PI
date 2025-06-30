from views.acoes_view import TelaAcoes

class AcoesController:
    def __init__(self,root):
        self.root = root 
        self.view = TelaAcoes(self)

    def iniciar_tela(self):
        self.view.mostrar()

    def abrir_cadastro_cliente(self):
        pass

    def abrir_cadastro_medico(self):
        pass

    def abrir_calcula_imc(self):
        pass

    def abrir_medir_pressao(self):
        pass

    def abrir_medir_hemoglobina(self):
        pass

    def abrir_dashboard(self):    
        pass