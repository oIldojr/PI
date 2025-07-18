from db import conectBD
class Clinica:
    def __init__(self,nome,cnpj,telefone,id = None):
        self.id = id 
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone

    def salvar_clinica():
    conn = conectBD()
    cursor = conn.cursor()

        if self.id is None:

            sql = """
            INSERT INTO clinica (nome,cnpj,telefone)
            VALUES (%s, %s, %s, %s)
            """
            valores = (self.nome, self.cnpj, self.telefone)

        else:
             sql = "UPDATE clinica SET nome=%s, cnpj=%s,telefone=%s WHERE id=%s)"

             valores = (self.nome, self.cnpj, self.telefone,self.id)

    conn.commit()
    cursor.close()
    conn.close()

    def deletar(self):
        if self.id is not None:
            conn =conectBD()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clinica WHERE id = %s",(self.id))    
            conn.commit()

        cursor.close()
        conn.close()

