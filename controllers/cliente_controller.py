from models.cliente_model import Cliente 

class ClienteController:
    def cadastrar_cliente(self,nome,email,data_nascimento,telefone):
        cliente = Cliente(nome,email,data_nascimento,telefone)
        cliente.salvar_cliente()
        return cliente

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