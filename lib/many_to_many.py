class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        books_list = [contract.book for contract in self.contracts()]
        return books_list
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(royalties)
    
class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.check_author(author)
        self.check_book(book)
        self.check_date(date)
        self.check_royalties(royalties)
        Contract.all.append(self)
    def check_author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self.author = author
    def check_book(self, book):
        if not isinstance(book, Book):
            raise Exception
        self.book = book
    def check_date(self, date):
        if not isinstance(date, str):
            raise Exception
        self.date = date
    def check_royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception
        self.royalties = royalties
    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)