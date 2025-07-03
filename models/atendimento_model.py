from db import conectBD

class Atendimento:
    def __init__(data_atendimento,id_descricao,id_agendamento,id = None):
        self.id = id 
        self.nome = nome
        self.email = email
        self.especialidade = especialidade
        self.telefone = telefone

    def salvar_atnedimento(self):
        conn = conectBD()
        cursor = conn.cursor()

        if self.id is None:

            sql = """
            INSERT INTO atendimento (data_atendimento,id_descricao,id_agendamento)
            VALUES (%s, %s, %s)
            """
            valores = (self.data_atendimento, self.id_agendamento, self.id_descricao, self.id)

        else:
             sql = "UPDATE atendimento SET data_atendimento=%s, id_descricao=%s,id_agendamento=%s WHERE id=%s)"

             valores = (self.data_atendimento, self.id_agendamento, self.id_descricao,self.id)

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
            conn = conectBD()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM atendimento")
            resultados = cursor.fetchall()

            cursor.close
            conn.close
            return[Atendimento(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id):
        conn = conectBD()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM atendimento WHERE id = %s",(id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

    
    def deletar(self):
            if self.id is not None:
                conn = conectBD()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM atendimento WHERE id = %s",(self.id))    
                conn.commit()

            cursor.close()
            conn.close()
             

  
