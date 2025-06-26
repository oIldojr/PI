from db import conectBD

def inserir_cliente(nome,email,data_nascimento,telefone ):
    conn = conectBD()
    cursor = conn.cursor()

    sql = """
    INSERT INTO clientes (nome, email,data_nascimento,telefone)
    VALUES (%s, %s, %s, %s)
    """
    valores = (nome, email, data_nascimento, telefone)
    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()
