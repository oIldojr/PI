from db import conectBD


class Agendamento:
    def __init__(data_agendamento,hora_agendamento,status,id_cliente,id_medico,id= None):
        self.data_agendamento = data_agendamento
        self.hora_agendamento = hora_agendamento
        self.status = status
        self.id_cliente = id_cliente
        self.id_medico = id_medico


    def salvar_agendamento(self):
        conn = conectBD()
        cursor = conn.cursor()

        if self.id is None:

            sql = """
            INSERT INTO agendamento (data_agendamento,hora_agendamento,status,id_cliente,id_medico)
            VALUES (%s, %s, %s, %s,%s)
            """
            valores = (self.data_agendamento, self.hora_agendamento, self.status, self.id_cliente,self.id_medico)

        else:
             sql = "UPDATE agendamento SET data_agendamento=%s, hora_agendamento=%s,status=%sid_cliente,id_medico=%s WHERE id=%s)"

             valores = (self.data_agendamento,self.hora_agendamento,self.status,self.id_cliente,self.id_medico)

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
            conn = conectBD()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM agendamento")
            resultados = cursor.fetchall()

            cursor.close()
            conn.close()
            return[Agendamento(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id):
        conn = conectBD()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM agendamento WHERE id = %s",(id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

    
    def deletar(self):
            if self.id is not None:
                conn = conectBD()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM agendamento WHERE id = %s",(self.id))    
                conn.commit()

            cursor.close()
            conn.close()

             
   