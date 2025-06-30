from models.cliente import Cliente 

class ClienteController:
    def cadastrar_cliente(self,nome,email,telefone,data_nascimento):
        cliente = Cliente(nome,email,telefone,data_nascimento)
        cliente.salvar()
        return cliente

    def listar_clientes(self):
        return cliente.buscar_todos

    def atualizar_cliente(self,id,nome,email,telefone,data_nascimento)
        cliente = Cliente(nome,email,telefone,data_nascimento,id)
        cliente.salvar()
        return cliente

    def excluir_cliente(self,id):
        cliente = Cliente.buscar_por_id(id)
        if cliente:
            cliente.deletar()
            return True 
        return False 

    def validar_email(self,email):
        return "@" in email and "." in email