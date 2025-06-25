from db import conectBD

def inserir_medico(nome,email,especialidade,telefone ):
    conn = conectBD()
    cursor = conn.cursor()

    sql = """
    INSERT INTO medicos (nome, email, especialidade, telefone)
    VALUES (%s, %s, %s, %s)
    """
    valores = (nome, email, especialidade, telefone)
    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()
