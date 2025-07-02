from models.cliente_model import Cliente
from views.clientes_view import TelaCadastroCliente

class ClienteController:
    def __init__(self, root):
        self.root = root
        self.view = TelaCadastroCliente(self.root, self)
        
    def iniciar_tela(self):
        self.view.mostrar()
    
    def cadastrar_cliente(self, nome, email, data_nascimento, telefone):
        try:
            if not self.validar_email(email):
                raise ValueError("E-mail inválido")
                
            cliente = Cliente(nome, email, data_nascimento, telefone)
            cliente.salvar_cliente()
            return cliente
        except Exception as e:
            raise 

    def listar_clientes(self):
        return Cliente.buscar_todos()

    def atualizar_cliente(self,id,nome,email,data_nascimento,telefone):
        cliente = Cliente(nome,email,data_nascimento,telefone,id)
        cliente.salvar_cliente()
        return cliente

    def excluir_cliente(self,id):
        cliente = Cliente.buscar_por_id(id)
        if cliente:
            cliente.deletar()
            return True 
        return False 

    def validar_email(self,email):
        return "@" in email and "." in email