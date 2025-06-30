from db import conectBD

class Medico:
    def __init__(self,nome,email,especialidade,telefone,id = None):
        self.id = id 
        self.nome = nome
        self.email = email
        self.especialidade = especialidade
        self.telefone = telefone

    def salvar_medico(self):
        conn = conectBD()
        cursor = conn.cursor()

        if self.id is None:

            sql = """
            INSERT INTO medicos (nome, email,especialidade,telefone)
            VALUES (%s, %s, %s, %s)
            """
            valores = (self.nome, self.email, self.especialidade, self.telefone)

        else:
             sql = "UPDATE medicos SET nome=%s, email=%s,especialidade=%s,telefone=%s WHERE id=%s)"

             valores = (self.nome, self.email, self.especialidade, self.telefone,self.id)

        conn.commit()
        cursor.close()
        conn.close()


     @staticmethod
    def buscar_todos():
            conn = conectar 
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM medicos")
            resultados = cursor.fetchall()

            cursor.close
            conn.close
            return[Medico(**r) for r in resultados]

     @staticmethod
     def buscar_por_id(id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM medicos WHERE id = %s",(id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

     
     def deletar(self):
            if self.id is not None:
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM medicos WHERE id = %s",(self.id))    
                conn.commit()
            cursor.close()
                conn.close
             
    

    
    