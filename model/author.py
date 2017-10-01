from base import Base
from sqlalchemy import Column, String, Integer

class Author(Base):
    __tablename__ = 'author'

    def __init__(self, id='', name='', last_name=''):
        super(Author, self).__init__()

        self.id = id
        self.name = name
        self.last_name = last_name

    id = Column(Integer, primary_key=True)
    name = Column(String(15))
    last_name = Column(String(25))

    # author = relationship("BookPerAuthor", backref="author", order_by="BookPerAuthor.id")

    # @staticmethod
    # def find_all():
    #     authors = []
    #     au = session.query(Author.id, Author.name, Author.last_name)
    #     for author in au:
    #         author = Author(author[0], author[1], author[2])
    #         authors.append(author)
    #     return authors

    # def insert(self):
    #     author_object = Author(self.id, self.name, self.last_name)
    #     session.add(author_object)
    #     session.commit()
        # cursor.execute("INSERT INTO author (id, name, last_name) VALUES (NULL, '{0}', '{1}')".format(self.name, self.last_name))
        # db.commit()
