from base import Base
from sqlalchemy import Column, Integer, Date, ForeignKey


class BookInVisitor(Base):
    __tablename__ = 'book_in_visitor'

    def __init__(self, id, taking_date, returning_date, visitor_id, book_id):
        super(BookInVisitor, self).__init__()

        self.id = id
        self.taking_date = taking_date
        self.returning_date = returning_date
        self.visitor_id = int(visitor_id)
        self.book_id = int(book_id)

    id = Column(Integer, primary_key=True)
    taking_date = Column(Date)
    returning_date = Column(Date)
    visitor_id = Column(ForeignKey('visitor.id'))
    book_id = Column(ForeignKey('book.id'))



    # @staticmethod
    # def find_all():
    #     history = []
    #     bookinvisitor = session.query(BookInVisitor.id, BookInVisitor.taking_date, BookInVisitor.returning_date,
    #                                   BookInVisitor.visitor_id, BookInVisitor.book_id)
    #     for bkinvs in bookinvisitor:
    #         bookvisitor = BookInVisitor(bkinvs[0], bkinvs[1], bkinvs[2], bkinvs[3], bkinvs[4])
    #         history.append(bookvisitor)
    #     return history

    # def insert(self):
    #     cursor.execute(
    #         "INSERT INTO book_in_visitor (id, taking_date, returning_date, visitor_id, book_id) VALUES (NULL, '{}',  NULL, {}, {})".format(
    #             self.data_of_take, self.visitor_id, self.book_id))
    #     cursor.execute("SELECT last_insert_id()")
    #     self.id = cursor.fetchall()[0][0]
    #     db.commit()

    # def update(self):
    #     cursor.execute(
    #         "UPDATE book_in_visitor SET returning_date = '{}' WHERE id = {}".format(self.remove_of_data, self.id))
    #     db.commit()


    # if len(lib.visitors) == 0:
    #     print("Visitor not exist")
    #     return exit
    # else:
    #     found_visitor = False
    #     for i in lib.visitors:
    #         if i.id == number_visitor_id:
    #             found_visitor = True
    #             if found_visitor == False:
    #                 print("Error visitor!")
    #                 return exit
    # if len(lib.books) == 0:
    #     print("Book not exist")
    #     return exit
    # else:
    #     found_book = False
    #     for j in lib.books:
    #         if j.id == number_book_id:
    #             found_book = True
    #             if found_book == False:
    #                 print("Error book!")
    #                 return exit
    #             else:
    #                 lib.add_data_of_remove(number_visitor_id, number_book_id, remove_date)
    # cursor.execute("UPDATE book_in_visitor SET returning_date = '{0}' WHERE visitor_id = {1} AND book_id = {2}".format(remove_date, number_visitor_id, number_book_id))
    # cursor.execute("SELECT available_count FROM book WHERE id = '{}'".format(number_book_id))
    # avbo = cursor.fetchall()
    # avbo = avbo[0][0]
    # result = int(avbo) + 1
    # cursor.execute("UPDATE book SET available_count = '{0}' WHERE id = '{1}'".format(result, number_book_id))
    # db.commit()
    # lib.add_data_of_remove(visitor_name, visitor_last_name, book_name, book_author_name, book_author_last_name, data)
    # found_visitor = False
    # for i in self.visitors:
    #     if i.id == number_visitor_id:
    #         found_visitor = True
    #         if found_visitor == True:
    #             visitor_name = i.name
    #             visitor_last_name = i.last_name
    #         else:
    #             print("Error visitor!")
    #             return exit
    # found_book = False
    # for j in self.books:
    #     if j.id == number_book_id:
    #         found_book = True
    #         if found_book != True:
    #             print("Error book!")
    #             return exit
    #         else:
    #             book_name = j.name
    #             book_author_name = j.author_name
    #             book_author_last_name = j.author_last_name
    #             lib.add_data_of_remove(visitor_name, visitor_last_name, book_name, book_author_name,
    #                                    book_author_last_name, remove_date)
