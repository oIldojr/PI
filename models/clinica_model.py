from db import conectBD

def inserir_():
    conn = conectBD()
    cursor = conn.cursor()

    sql = """
    INSERT INTO medicos ()
    VALUES ()
    """
    valores = ()
    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()
