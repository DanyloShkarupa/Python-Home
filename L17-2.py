class Author:

    def __init__(self, name, country, birthday, books=[]):
        self.books = books
        self.birthday = birthday
        self.country = country
        self.name = name

    def __repr__(self):
        return f'The object Author: {self.name}'

    def __str__(self):
        return f'name: {self.name}\n' \
               f' country: {self.country}\n' \
               f' birthday: {self.birthday}\n' \
               f' books: {self.books}\n'

    def append_book(self, name):
        self.books.append(name)


class Library:
    def __init__(self, name, books=[], authors=[]):
        self.authors = authors
        self.books = books
        self.name = name

    def __repr__(self):
        return f'The object Library "{self.name}"'

    def __str__(self):
        return f'name: {self.name}\n' \
               f'books: {self.books}\n' \
               f'authors: {self.authors}\n'

    def new_book(self, name: str, year: int, author: Author):
        author.append_book(name)
        new_book = Book(name, year, author)
        self.books.append(new_book)
        return new_book

    def group_by_author(self, author: Author):
        return author.books

    def group_by_year(self, year: int):
        return [x['name'] for x in list(filter(lambda book: book['year'] == year, Book.BOOKS))]


class Book:
    BOOKS = []
    COUNT_BOOKS = len(BOOKS)

    def __init__(self, name, year, author):
        self.BOOKS.append({'name': name, 'year': year, 'author': author})
        self.author = author
        self.year = year
        self.name = name

    def __repr__(self):
        return f'{self.name}'
    #
    def __str__(self):
        return f'{self.name}'


author1 = Author('J. K. Rowling', 'England', 1965, ['Harry Potter 1',
                                                    'Harry Potter 2',
                                                    'Harry Potter 3',
                                                    'Harry Potter 4',
                                                    'Harry Potter 5',
                                                    'Harry Potter 6',
                                                    'Harry Potter 7'])
author2 = Author('Matt Haig', 'England', 1975, ['The Midnight Library', ])
lib = Library('Classic',

              ['Harry Potter 1',
               'Harry Potter 2',
               'Harry Potter 3',
               'Harry Potter 4',
               'Harry Potter 5',
               'Harry Potter 6',
               'Harry Potter 7',
               'The Midnight Library'],

              ['J. K. Rowling',
               'Matt Haig'])

lib.new_book('The Dead Fathers Club', 2006, author2)

print(lib.group_by_author(author1))
print(lib.group_by_author(author2))

lib.new_book('Python3', 2006, author2)

print(lib.group_by_year(2006))

print(author2)

print(lib, author1)


