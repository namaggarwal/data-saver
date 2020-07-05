from sqlalchemy import MetaData, Table, Column, Integer, String


class Books(object):
    def __init__(self, name):
        meta = MetaData()

        Books.books = Table(
            'books', meta,
            Column('id', Integer, primary_key=True),
            Column('name', String),
        )

        self.name = name

    def save(self, conn):
        ins = Books.books.insert().values(name=self.name)
        conn.execute(ins)
