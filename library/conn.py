from PySide6 import QtSql


class Data:
    def __init__(self):
        super().__init__()

        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('notebook_db.db')

        if not db.open():
            return False

        query = QtSql.QSqlQuery()
        query.exec('CREATE TABLE IF NOT EXISTS notes'
                   '(ID integer primary key AUTOINCREMENT,'
                   'Title VARCHAR(20),'
                   'Description VARCHAR(100),'
                   'DateTime DATETIME,'
                   'Level VARCHAR(20))')
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_note_query(self, title, description, datetime, level):
        sql_query = "INSERT INTO notes (Title, Description, DateTime, Level) VALUES (?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [title, description, datetime, level])

    def edit_note_query(self, title, description, datetime, level, id):
        sql_query = 'UPDATE notes SET Title=?, Description=?, DateTime=?, Level=? WHERE ID=?'
        self.execute_query_with_params(sql_query, [title, description, datetime, level, id])

    def delete_note_query(self, id):
        sql_query = 'DELETE FROM notes WHERE ID=?'
        self.execute_query_with_params(sql_query, [id])
