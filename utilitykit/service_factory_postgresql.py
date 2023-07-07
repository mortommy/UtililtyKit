import pathlib


def load_pg_table_from_csv_file(connection, replace: bool, file_path_name: str, table_name: str, schema: str,
                                csv_file_separator: str = ';', encoding='utf-8') -> None:
    """
    Loads data from a csv file to a PostgreSQL table. Load data from a csv is the faster way. The destination table must exists.

    :param connection: psycopg2 connection
    :param schema: optional destination table schema
    :param encoding: csv file encoding format, utf-8 is the default
    :param csv_file_separator: csv file separator
    :param replace: if true, data in the destination table is overwritten
    :param file_path_name: csv file full path and name
    :param table_name: destination table name
    """
    cf = pathlib.Path(file_path_name)
    if not cf.exists():
        raise Exception('File ' + file_path_name + 'does not exist.')
    try:
        cur = connection.cursor()
        dest_table = table_name
        if schema != '':
            dest_table = schema + '.' + table_name
        if replace:
            sql = 'TRUNCATE TABLE ' + dest_table + ";"
            cur.execute(sql)

        sql = "COPY " + dest_table + " FROM STDIN DELIMITER '" + csv_file_separator + "' CSV HEADER;"
        f = open(file_path_name, 'r', encoding=encoding)
        cur.copy_expert(sql, f)
        connection.commit()
        f.close()
        cur.close()
    except Exception as e:
        raise Exception(e)


def call_pg_procedure(connection, procedure_name: str, parameters: tuple = None, schema: str = ''):
    """
    Call a procedure saved in a PostgreSQL database.
    :param connection: psycopg2 connection
    :param procedure_name: procedure name
    :param parameters: optional, procedure parameters, as tuples of values
    :param schema: optional, procedure schema
    """
    if procedure_name == '':
        raise Exception('Procedure name cannot be empty.')
    try:
        cur = connection.cursor()
        if schema != '':
            procedure_name = schema + '.' + procedure_name
        command = 'CALL ' + procedure_name + '('
        if parameters is not None:
            for p in parameters:
                command = command + '%s',
            command = command[0:-1]
        command = command + ');'
        cur.execute(command, parameters)
        connection.commit()
        cur.close()
    except Exception as e:
        raise Exception(e)
