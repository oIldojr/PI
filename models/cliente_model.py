from db import conectBD

class Cliente:
    def __init__(self,nome,email,data_nascimento,telefone,id = None):
        self.id = id 
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.telefone = telefone

    def salvar_cliente(self):
        conn = conectBD()
        cursor = conn.cursor()

        if self.id is None:

            sql = """
            INSERT INTO clientes (nome, email,data_nascimento,telefone)
            VALUES (%s, %s, %s, %s)
            """
            valores = (self.nome, self.email, self.data_nascimento, self.telefone)

        else:
             sql = "UPDATE clientes SET nome=%s, email=%s,data_nascimento=%s,telefone=%s WHERE id=%s)"

             valores = (self.nome, self.email, self.data_nascimento, self.telefone,self.id)

     @staticmethod
    def buscar_todos():
            conn = conectar 
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM clientes")
            resultados = cursor.fetchall()

            cursor.close
            conn.close
            return[Cliente(**r) for r in resultados]

     @staticmethod
     def buscar_por_id(id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM clientes WHERE id = %s"(id))
        resultado = cursor.fetchone()

        cursor.close
        conn.close()

    
     def deletar(self):
            if self.id is not None:
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM clientes WHERE id = %s",(self.id))    
                conn.commit()
                cursor.close()
                conn.close
             

             
        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()
