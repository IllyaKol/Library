import pymysql
from base import engine
from sqlalchemy.orm import Session
from author import Author
from book import Book
from book_in_visitor import BookInVisitor
from book_per_author import BookPerAuthor
from gender import Gender
from visitor import Visitor


class Library(object):
    def __init__(self):
        super(Library, self).__init__()

        self.db = pymysql.connect("localhost", "root", "***********", "library_system")
        self.session = Session(bind=engine)

        self.number_of_library = ''  # library_number
        self.street = ''
        self.phone_number = 0
        self.books = self.find_all_book()
        self.visitors = self.find_all_visitor()
        self.history = self.find_all_book_in_visitor()
        self.authors = self.find_all_author()
        self.book_has_author_list = self.find_all_book_has_author()
        self.genders = self.find_all_gender()

        if len(self.genders) == 0:
            self.initialize_database()

    def add_visitor(self, visitor):
        for i in self.visitors:
            if i.name == visitor.name and i.last_name == visitor.last_name and i.number == visitor.number:
                print('Visitor exist!')
                return False
        else:
            self.visitors.append(visitor)
            return True

    def edit_visitors(self, number_id, new_name, new_last_name, new_number):
        visi = self.session.query(Visitor).get(number_id)
        visi.name = new_name
        visi.lsat_name = new_last_name
        visi.number = new_number

    def add_visitor_to_bd(self, number_id, first_name, second_name, birth_date, number, gender):

        # found = False
        for i in self.visitors:
            if int(number_id) == i.id:
                # found = True
                print("This id use")
                return
        # if found == True:
        #     print("This id use")
        #     return exit
        # else:
        #     if gender == 1:
        #         pass
        #     elif gender == 2:
        #         pass
        #     else:
        #         print('Error: gender_id!')
        #         return exit
        visit = Visitor(number_id, first_name, second_name, birth_date, number, gender)
        if self.add_visitor(visit) == False:
            return
        self.session.add(visit)
        self.session.commit()
        print('This visitor has been added')

    def add_book_to_bd(self, book_id, name_book, author_name, author_last_name, book_date, count):

        found_book = False  # because it could change the variable found on True after checking the author
        for book in self.books:
            if book.name == name_book:
                found_book = True
                print('This book exist')
        if found_book == True:
            return
        found = False
        for author in self.authors:
            if author.name == author_name and author.last_name == author_last_name:
                found = True
                aid = author.id
                self.db.commit()
        if not found:
            author = Author(None, author_name, author_last_name)
            self.session.add(author)
            self.session.commit()
            aid = author.id
            author.id = aid
            self.authors.append(author)
            self.db.commit()
        if not found_book:
            available_count = count
            book = Book(book_id, name_book, book_date, count, available_count)
            self.session.add(book)
            self.session.commit()
            book_per_author = BookPerAuthor(None, book_id, aid)
            self.session.add(book_per_author)
            self.session.commit()
            self.book_has_author_list.append(book_per_author)
            self.books.append(book)
            self.db.commit()
            print('This book has been added')

    def add_remove_date(self, visitor_id, book_id, returning_date):

        for i in self.history:
            if int(visitor_id) == int(i.visitor_id) and int(book_id) == int(i.book_id) and i.returning_date is None:
                i.returning_date = returning_date
                # session.query(BookInVisitor).filter(BookInVisitor.visitor_id == visitor_id and
                # BookInVisitor.book_id == book_id).update({"returning_date":returning_date})
                self.session.commit()

                book = self.session.query(Book).get(book_id)
                book.available_count += 1
                self.session.query(Book).filter(Book.id == book_id).update({"available_count": book.available_count})
                self.session.commit()

    def write_book_on_visitor_to_bd(self, visitor_id, book_id, taking_date):

        object_book_in_visitor = BookInVisitor(None, taking_date, None, visitor_id, book_id)
        self.session.add(object_book_in_visitor)
        self.session.commit()

        book = self.session.query(Book).get(book_id)
        book.available_count -= 1
        self.session.query(Book).filter(Book.id == book_id).update({"available_count": book.available_count})
        self.session.commit()

        self.history.append(object_book_in_visitor)

    def change_visitor(self, number_id, new_name, new_last_name, new_number):

        self.session.query(Visitor).filter(Visitor.id == number_id).update({"name": new_name,
                                                                            "last_name": new_last_name,
                                                                            "number": new_number})
        self.session.commit()

        self.edit_visitors(number_id, new_name, new_last_name, new_number)
        print('Changes done.')

    def initialize_database(self):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO gender (id, name) VALUES (NULL, 'male')")
        cursor.execute("INSERT INTO gender (id, name) VALUES (NULL, 'female')")
        self.db.commit()
        gender = Gender(1, 'male')
        self.genders.append(gender)
        gender1 = Gender(2, 'female')
        self.genders.append(gender1)

    def find_all_book(self):
        return self.session.query(Book).all()

    def find_all_visitor(self):
        visitors = []
        vs = self.session.query(Visitor).all()
        for visitor in vs:
            visitor = Visitor(visitor.id, visitor.name, visitor.last_name, visitor.birth_date, visitor.number,
                              visitor.gender_id)
            visitors.append(visitor)
        return vs

    def find_all_book_in_visitor(self):
        history = []
        bookinvisitor = self.session.query(BookInVisitor).all()
        for bkinvs in bookinvisitor:
            bookvisitor = BookInVisitor(bkinvs.id, bkinvs.taking_date, bkinvs.returning_date, bkinvs.visitor_id,
                                        bkinvs.book_id)
            history.append(bookvisitor)
        return bookinvisitor

    def find_all_author(self):
        authors = []
        au = self.session.query(Author).all()
        for author in au:
            author = Author(author.id, author.name, author.last_name)
            authors.append(author)
        return au

    def find_all_book_has_author(self):
        book_has_author_list = []
        all_from_book_has_author = self.session.query(BookPerAuthor).all()
        for id in all_from_book_has_author:
            id = BookPerAuthor(id.id, id.book_id, id.author_id)
            book_has_author_list.append(id)
        return all_from_book_has_author

    def find_all_gender(self):
        genders = []
        g = self.session.query(Gender).all()
        for gender in g:
            object_gender = Gender(gender.id, gender.name)
            genders.append(object_gender)
        return g
