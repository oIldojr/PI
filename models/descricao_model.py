from db import conectBD

class Descricao:
    def __init__(self,sintomas,observacoes,descricao_atendimento,id = None):
        self.id = id 
        self.descricao_atendimento = descricao_atendimento
        self.observacoes = observacoes
        self.sintomas = sintomas

    def salvar_descricao(self):
    conn = conectBD()
    cursor = conn.cursor()
    
        if self.id is None:

            sql = """
            INSERT INTO descricao_atendimento (sintomas,observacoes,descricao_atendimento)
            VALUES (%s, %s, %s)
            """
            valores = (self.descricao_atendimento,self.observacoes,self.sintomas)

        else:
             sql = "UPDATE descricao_atendimento SET sintomas=%s,observacoes=%s,descricao_atendimento=%s WHERE id=%s)"

             valores = (self.descricao_atendimento,self,sintomas,self.observacoes,self.id)

    conn.commit()
    cursor.close()
    conn.close()

    @staticmethod
    def buscar_todos():
            conn = conectBD()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM descricao_atendimento")
            resultados = cursor.fetchall()

            cursor.close
            conn.close
            return[Descricao(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id):
        conn = conectBD()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM descricao_atendimento WHERE id = %s",(id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

     
    def deletar(self):
            if self.id is not None:
                conn = conectBD()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM descricao_atendimento WHERE id = %s",(self.id))    
                conn.commit()
           
            cursor.close()
            conn.close()
             

    
   