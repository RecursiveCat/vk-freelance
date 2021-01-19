import sqlite3


class Sql:

    def __init__(self,path_to_db):
        self.data_base_path       = str(path_to_db)
        self.data_base_connection = sqlite3.connect(self.data_base_path)
        self.data_base_cursor     = self.data_base_connection.cursor()

    def run(self,command):
        self.data_base_last_query = str(command)
        return self.data_base_cursor.execute(str(command))

    def set_query_after_restart(self,query):
        return self.query_after_restart = string(query)

    def fetch():
        return self.cursor.fetchall()
