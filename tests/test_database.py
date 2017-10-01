from unittest import TestCase
# import pymysql
# from sqlalchemy.orm import Session
# from model.base import engine
# from model.book import Book
# from model.book_in_visitor import BookInVisitor
from model.library import Library


class TestDatabase(TestCase):
    def setUp(self):
        self.library = Library()

    def test_find_all_books(self):
        books = self.library.find_all_book()
        self.assertIsNotNone(books)

    def test_book_relationship(self):
        books = self.library.find_all_book()
        first_book = books[0]
        first_author = first_book.book_has_author[0]
        self.assertIsNotNone(first_author.author.name)

