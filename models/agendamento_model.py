from db import conectBD

def agendar_agendamento(data_agendamento,hora_agendamento,status,id_cliente,id_medico):
    conn = conectBD()
    cursor = conn.cursor()

    sql = """
    INSERT INTO agendamento (data_agendamento,hora_agendamento,status,id_cliente,id_medico)
    VALUES (%s, %s, %s, %s,%s)
    """
    valores = (data_agendamento,hora_agendamento,status,id_cliente,id_medico)
    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()
