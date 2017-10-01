from model.library import Library
import zbar


def scan_visitor_id():
    print('Enter visitor code:')
    proc = zbar.Processor()
    proc.parse_config('enable')
    device = '/dev/video0'
    proc.init(device)
    proc.visible = True
    proc.process_one()
    proc.visible = False
    for symbol in proc.results:
        visitor_id = symbol.data
        visitor_id = int(visitor_id)
        print (visitor_id)
        return (visitor_id)


def scan_book_id():
    print('Enter book code:')
    proc = zbar.Processor()
    proc.parse_config('enable')
    device = '/dev/video0'
    proc.init(device)
    proc.visible = True
    proc.process_one()
    proc.visible = False
    for symbol in proc.results:
        book_id = symbol.data
        book_id = int(book_id)
        print (book_id)
        return (book_id)


if __name__ == "__main__":
    lib = Library()

    while True:
        number = int(input(
            '1 - Show all books\n2 - Show all visitors\n3 - Add visitor\n4 - Add book\n5 - Show author\n6 - Change visitor\n7 - Write book on visitor\n8 - Add remove date\n9 - Show history\n10 - Serch book by name\n11 - Search book by author\n12 - Show books in visitor\n:'))
        if number == 1:
            if len(lib.books) == 0:
                print('Our library has not book')
            for book in lib.books:
                for book_has_author in lib.book_has_author_list:
                    if book_has_author.book_id == book.id:
                        author_id = book_has_author.author_id
                for author in lib.authors:
                    if author_id == author.id:
                        author_name = author.name
                        author_last_name = author.last_name
                print(
                    'ID: {}, Book name: {}, Date: {}, Author name: {}, Author last name: {}'.format(book.id, book.name,
                                                                                                    book.date,
                                                                                                    author_name,
                                                                                                    author_last_name))
        elif number == 2:
            if len(lib.visitors) == 0:
                print('Our library has not visitors')
            for i in lib.visitors:
                for gender in lib.genders:
                    if gender.id == i.gender_id:
                        gender_name = gender.name
                        print(
                            'ID: ' + str(
                                i.id) + ', Name: ' + i.name + ', last name: ' + i.last_name + ', birth date: ' +
                            str(i.birth_date) + ', number: ' + str(i.number) + ', gender: ' + gender_name)
        elif number == 3:
            first_name = raw_input('Enter name: ')
            first_name = first_name.capitalize()
            second_name = raw_input('Enter last_name: ')
            second_name = second_name.capitalize()
            birth_date = raw_input('Enter birth date(yyyy-mm-dd): ')
            number = raw_input('Enter your number(380** *** *** *): ')
            genders_id_name = ''
            for gender in lib.genders:
                genders_id_name += '{gender.id}-{gender.name} / '.format(gender=gender)
            gender = raw_input('Enter ' + genders_id_name + ': ')
            gender = int(gender)

            lib.add_visitor_to_bd(scan_visitor_id(), first_name, second_name, birth_date, number, gender)
        elif number == 4:
            name_book = raw_input('Enter book name: ')
            name_book = name_book.capitalize()
            author_name = raw_input('Enter author name: ')
            author_name = author_name.capitalize()
            author_last_name = raw_input('Enter author last name: ')
            author_last_name = author_last_name.capitalize()
            book_date = raw_input('Enter date(yyyy-mm-dd): ')
            count = raw_input('Enter count:')

            lib.add_book_to_bd(scan_book_id(), name_book, author_name, author_last_name, book_date, count)
        elif number == 5:
            if len(lib.authors) == 0:
                print("Author do not exist")
            for i in lib.authors:
                print('ID: ' + str(i.id) + ', name author: ' + i.name + ', last name: ' + i.last_name)
        elif number == 6:
            new_name = raw_input('Enter new name visitor: ')
            new_name = new_name.capitalize()
            new_last_name = raw_input('Enter new last name visitor: ')
            new_last_name = new_last_name.capitalize()
            new_number = raw_input('Enter new number visitor: ')

            lib.change_visitor(scan_visitor_id(), new_name, new_last_name, new_number)
        elif number == 7:
            taking_date = raw_input('Enter date take(yyyy-mm-dd): ')

            lib.write_book_on_visitor_to_bd(scan_visitor_id(), scan_book_id(), taking_date)

            # visitor_name = raw_input('Enter visitor name: ')
            # visitor_name = visitor_name.capitalize()
            # visitor_last_name = raw_input('Enter visitor last name: ')
            # visitor_last_name = visitor_last_name.capitalize()
            # vis = lib.find_visitor_by_name(visitor_name, visitor_last_name)
            # data_take = raw_input('Enter data take(yyyy-mm-dd): ')
            # if vis == None:
            #     print('Enter again visitor')
            #     break
            # else:
            #     book_name = raw_input('Enter book name: ')
            #     book_name = book_name.capitalize()
            #     book_author_name = raw_input('Enter author name: ')
            #     book_author_name = book_author_name.capitalize()
            #     book_author_last_name = raw_input('Enter author last name: ')
            #     book_author_last_name = book_author_last_name.capitalize()
            #     bo = lib.find_book_by_name(book_name, book_author_name, book_author_last_name)
            #     if bo == None:
            #         print('Enter again book')
            #         break
            #     else:
            #         cursor.execute("SELECT available_count FROM book WHERE name = '{}'".format(book_name))
            #         avcoif = cursor.fetchall()
            #         avcoif = avcoif[0][0]
            #         if avcoif == 0:
            #             print("This book is not available!")
            #         else:
            #             lib.write_book_visitor(vis, bo, data_take)
            #             cursor.execute("SELECT id FROM visitor WHERE name = '{0}' AND last_name = '{1}'".format(visitor_name, visitor_last_name))
            #             idvisitor = cursor.fetchall()
            #             idvisitor = idvisitor[0][0]
            #             # print(idvisitor)
            #             cursor.execute("SELECT id FROM book WHERE name = '{}'".format(book_name))
            #             idbook = cursor.fetchall()
            #             idbook = idbook[0][0]
            #             # print(idbook)
            #             cursor.execute("INSERT INTO book_in_visitor (id, taking_date, returning_date, visitor_id, book_id) VALUES (NULL, '{0}', {1}, {2}, {3})".format(data_take, 'NULL', idvisitor, idbook))
            #             cursor.execute("SELECT available_count FROM book WHERE id = {}".format(idbook))
            #             avco = cursor.fetchall()
            #             # print(avco)
            #             avco = avco[0][0]
            #             # print(avco)
            #             result = int(avco) - 1
            #             cursor.execute("UPDATE book SET available_count = '{0}' WHERE id = {1}".format(result, idbook))
            #             db.commit()
        elif number == 8:
            returning_date = raw_input('Enter data remove(yyyy-mm-dd): ')

            lib.add_remove_date(scan_visitor_id(), scan_book_id(), returning_date)
        elif number == 9:
            if len(lib.history) == 0:
                print("History empty")
            else:
                for i in lib.history:
                    for visitor in lib.visitors:
                        if i.visitor_id == int(visitor.id):
                            break
                    for book in lib.books:
                        if i.book_id == int(book.id):
                            break
                    for author_per_book in lib.book_has_author_list:
                        if i.book_id == int(author_per_book.book_id):
                            break
                    for author in lib.authors:
                        if author_per_book.author_id == author.id:
                            break
                    print('Visitor: ' + visitor.name + ' ' + visitor.last_name + ', take: ' + book.name + ', author: '
                          + author.name + ' ' + author.last_name + ', taking date: ' + str(i.taking_date) +
                          ', returning date: ' + str(i.returning_date))
        elif number == 10:
            i = raw_input("Enter book name: ")
            i = i.capitalize()
            found = False
            for book in lib.books:
                if book.name == i:
                    for book_author in lib.book_has_author_list:
                        if book.id == book_author.book_id:
                            break
                    for author in lib.authors:
                        if author.id == book_author.author_id:
                            break
                    print('ID: ' + str(book.id) + ', Book: ' + book.name + ', available count: ' +
                          str(book.available_count) + ', Author: ' + author.name + ' ' + author.last_name)
            found = True
            if not found:
                print("Not found")
        elif number == 11:
            author_name = raw_input("Enter author name: ")
            author_name = author_name.capitalize()
            author_last_name = raw_input("Enter author last name: ")
            author_last_name = author_last_name.capitalize()
            found = False
            for author in lib.authors:
                if author.name == author_name and author.last_name == author_last_name:
                    for book_author in lib.book_has_author_list:
                        if book_author.author_id == author.id:
                            for book in lib.books:
                                if book_author.book_id == book.id:
                                    break
                            print('ID: ' + str(book.id) + ', Book: ' + book.name + ', available count:' +
                                  str(book.available_count) + ', Author: ' + author.name + ' ' + author.last_name)
            found = True
            if not found:
                print("Not found")
        elif number == 12:
            visitor_name = raw_input("Enter visitor name: ")
            visitor_name = visitor_name.capitalize()
            visitor_last_name = raw_input("Enter visitor last name: ")
            visitor_last_name = visitor_last_name.capitalize()
            for visitor in lib.visitors:
                if visitor_name == visitor.name and visitor_last_name == visitor.last_name:
                    for i in lib.history:
                        if visitor.id == i.visitor_id:
                            for book in lib.books:
                                if i.book_id == book.id:
                                    break
                            for author_per_book in lib.book_has_author_list:
                                if book.id == author_per_book.book_id:
                                    break
                            for author in lib.authors:
                                if author_per_book.author_id == author.id:
                                    break
                            print('Name: ' + visitor.name + ', last name: ' + visitor.last_name + ', take book: ' +
                                  book.name + ', author: ' + author.name + ' ' + author.last_name + ', taking date:' +
                                  str(i.taking_date) + ', returning date: ' + str(i.returning_date))
