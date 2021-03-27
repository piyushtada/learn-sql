def drop_tables(cur, conn):
    """
    The function to drop database

    Parameters:
        cur  : The cursor that will be used to execute queries.
        conn : The connection towards current connecting database.
    """

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    The function to drop database

    Parameters:
        cur  : The cursor that will be used to execute queries.
        conn : The connection towards current connecting database.
    """

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()