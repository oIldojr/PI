from db import conectBD

def inserir_descricao(sintomas,observacoes,descricao_atendimento):
    conn = conectBD()
    cursor = conn.cursor()

    sql = """
    INSERT INTO descricao_atendimento (sintomas,observacoes,descricao_atendimento)
    VALUES (%s, %s, %s, %s)
    """
    valores = (sintomas,observacoes,descricao_atendimento)
    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()
