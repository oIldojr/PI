from models.medicos_model import Medico
from views.medicos_view import TelaCadastroMedico

class MedicoController:
    def __init__(self, root):
        self.root = root
        self.view = TelaCadastroMedico(self.root, self)
        
    def iniciar_tela(self):
        self.view.mostrar()
    
    def cadastrar_medico(self, nome, email, especialidade, telefone):
        try:
            if not self.validar_email(email):
                raise ValueError("E-mail inválido")
                
            medico = Medico(nome, email, especialidade, telefone)
            medico.salvar_medico()
            return medico
        except Exception as e:
            raise 

    def listar_medico(self):
        return Medico.buscar_todos()

    def atualizar_medico(self,id,nome,email,especialidade,telefone):
        medico = Medico(nome,email,especialidade,telefone,id)
        Medico.salvar_medico()
        return medico

    def excluir_medico(self,id):
        medico = Medico.buscar_por_id(id)
        if medico:
            medico.deletar()
            return True 
        return False 

    def validar_email(self,email):
        return "@" in email and "." in email