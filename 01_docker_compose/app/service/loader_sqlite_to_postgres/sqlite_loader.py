class SQLiteLoader(object):
    def __init__(self, cursor):
        self._cursor = cursor

    def load_data(self, table, dataclass_dict, load_rows_size=1):
        query = 'SELECT * FROM {table};'.format(
            table=table,
        )
        self._cursor.execute(query)
        while True:
            loaded_data = self._cursor.fetchmany(load_rows_size)
            if not loaded_data:
                break
            yield [dataclass_dict[table](**row) for row in loaded_data]
