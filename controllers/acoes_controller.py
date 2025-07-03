from views.acoes_view import TelaAcoes
from views.clientes_view import TelaCadastroCliente 
from controllers.cliente_controller import ClienteController 
from controllers.medico_controller import MedicoController
from views.medicos_view import TelaCadastroMedico
import tkinter as tk
from views.imc_view import TelaIMC

class AcoesController:
    def __init__(self, root):
        self.root = root
        self.view = TelaAcoes(self.root, self)

    def iniciar_tela(self):
        self.view.mostrar()

    def abrir_cadastro_cliente(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        
        controller = ClienteController(cadastro_window)
        
        cadastro_window.master = self.root 
        self.root.withdraw()  
    
        controller.iniciar_tela()

    def abrir_cadastro_medico(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        
        controller = MedicoController (cadastro_window)
        
        cadastro_window.master = self.root 
        self.root.withdraw()  
    
        controller.iniciar_tela()

    def abrir_calcula_imc(self):
        TelaIMC(self.root)
        self.root.withdraw()  
    

    def abrir_medir_pressao(self):
        pass

    def abrir_medir_hemoglobina(self):
        pass

    def abrir_dashboard(self):
        pass