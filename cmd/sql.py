import sqlite3


class Sql:

    def __init__(self,path_to_db)
        self.data_base = sqlite3.connect(path_to_db)
        self.cursor = self.data_base.cursor()

    def run(self,command):
        return self.cursor.execute(str(command))

    def set_query_after_restart(self,query):
        return self.query_after_restart = string(query)

    def fetch():
        return self.cursor.fetchall()
