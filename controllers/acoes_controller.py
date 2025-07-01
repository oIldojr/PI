from views.acoes_view import TelaAcoes
from views.clientes_view import TelaCadastroCliente 
from controllers.cliente_controller import ClienteController 

class AcoesController:
    def __init__(self, root):
        self.root = root
        self.view = TelaAcoes(self)

    def iniciar_tela(self):
        self.view.mostrar()

    def abrir_cadastro_cliente(self):
        cliente_controller = ClienteController()
        tela_cadastro_cliente = TelaCadastroCliente(cliente_controller, self.root)
        self.root.withdraw()  
        tela_cadastro_cliente.mostrar() 

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