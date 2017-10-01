from base import Base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'book'

    def __init__(self, id, name, date, count='', available_count=''):
        super(Book, self).__init__()

        self.id = int(id)
        self.name = name
        self.date = date
        self.count = int(count)
        self.available_count = int(available_count)

    id = Column(Integer, primary_key=True)
    name = Column(String(15))
    date = Column(Date)
    count = Column(Integer)
    available_count = Column(Integer)

    book_in_visitor = relationship("BookInVisitor", backref="book", order_by="BookInVisitor.id")
    book_has_author = relationship("BookPerAuthor", backref="book", order_by="BookPerAuthor.id")
    book_author = relationship('BookPerAuthor')
    history = relationship('BookInVisitor')

    # @staticmethod
    # def find_all():
    #     books = []
    #     bk = session.query(Book.id, Book.name, Book.date, Book.count, Book.available_count)
    #     for book in bk:
    #         book = Book(book[0], book[1], book[2], book[3], book[4])
    #         books.append(book)
    #     return books

    # def insert(self):
    #     book_object = Book(self.id, self.name, self.date, self.count, self.available_count)
    #     session.add(book_object)
    #     session.commit()
        # cursor.execute("INSERT INTO book (id, name, date, count, available_count) VALUES ({0}, '{1}', '{2}', {3}, {4})".format(self.id, self.name, self.date, self.count, self.available_count))
        # db.commit()

    # def update(self):
    #     cursor.execute("UPDATE book SET name = '{}', available_count = {} WHERE id = {}".format(self.name, self.available_count, self.id))
    #     db.commit()
