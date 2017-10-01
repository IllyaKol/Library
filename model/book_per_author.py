from base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class BookPerAuthor(Base):
    __tablename__ = 'book_has_author'

    def __init__(self, id, book_id='', author_id=''):
        super(BookPerAuthor, self).__init__()

        self.id = id
        self.book_id = book_id
        self.author_id = author_id

    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('book.id'))
    author_id = Column(ForeignKey('author.id'))

    # book_in_visitor = relationship("BookInVisitor", backref="book", order_by="BookInVisitor.id")
    # author = relationship("Author", backref="book_has_author", order_by="Author.id")
    author = relationship("Author", foreign_keys=[author_id])

    # @staticmethod
    # def find_all():
    #     book_has_author_list = []
    #     all_from_book_has_author = session.query(BookPerAuthor.id, BookPerAuthor.book_id, BookPerAuthor.author_id)
    #     for id in all_from_book_has_author:
    #         id = BookPerAuthor(id[0], id[1], id[2])
    #         book_has_author_list.append(id)
    #     return book_has_author_list

    # def insert(self):
    #     book_per_author_object = BookPerAuthor(None, self.book_id, self.author_id)
    #     session.add(book_per_author_object)
    #     session.commit()
    # cursor.execute(
    #     "INSERT INTO book_has_author (id, book_id, author_id) VALUES (NULL, {0}, {1})".format(self.book_id, self.author_id))
    # db.commit()
