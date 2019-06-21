from user import User
from book import Book, Fiction, Non_Fiction


"""
Create TomeRater class
"""
class TomeRater(object):
    def __init__(self):
        self.users= {}
        self.books= {}

    """
    Dunder methods for TomeRater class
    """
    def __repr__(self):
        count_books = len(self.books)
        count_users = len(self.users)
        return "This instance of TomeRater has {books} books and {users} users.".format(books=count_books,users=count_users)

    def __eq__(self, other_tome_rater):
        if isinstance(other_tome_rater, TomeRater):
            return self.books == other_tome_rater.books and self.users == other_tome_rater.users
        else:
            print("Supplied object is not valid TomeRater")

    """
    class methods
    """
    def isbn_exists_check(self, isbn):
        """
        Check if the ISBN no already exists in current Tome Rater instance
        """
        if len([book for book in self.books.keys() if isbn == book.get_isbn()]) > 0:
            return True
        else:
            return False

    def create_book(self, title, isbn, price):
        """
        Return book object with title and isbn
        """
        if self.isbn_exists_check(isbn=isbn):
            print("Existing isbn number: {}".format(isbn))
        else:
            return Book(title=title, isbn=isbn, price=price)

    def create_novel(self, title, isbn, price, author):
        """
        Return Fiction object with title, isbn, price and author
        """
        if self.isbn_exists_check(isbn=isbn):
            print("Existing isbn number: {isbn}".format(isbn=isbn))
        else:
            return Fiction(title=title, isbn=isbn, price=price, author=author)

    def create_non_fiction(self, title, isbn, price, subject, level):
        """
        Returns Non Fiction objects created with parameters passed
        """
        if self.isbn_exists_check(isbn=isbn):
            print("Existing isbn number: {}".format(isbn))
        else:
            return Non_Fiction(title=title, isbn=isbn, price=price, subject=subject, level=level)

    def add_book_to_user(self, book, email, rating=None):
        """
        Update user instance add book to users read book list
        Update user instance add rating if supplied
        Upate book instance add no of reads
        """
        if self.users.get(email):
            self.users.get(email).read_book(book=book, rating=rating)
            book.add_rating(rating=rating)
            no_of_reads = self.books.get(book, 0) + 1
            self.books.update({book: no_of_reads})
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        """
        Add new user to current instance of Tome rater
        if a list of books supplied add each book to user
        """
        try:
            if self.users.get(email):
                print("user with email: {email} already exists".format(email=email))
            else:
                self.users.update({email: User(name=name, email=email)})
                if user_books:
                    for book in user_books:
                        self.add_book_to_user(book=book, email=email)
        except Exception as e:
            print("""Failed to add user {name} with email {email}.
                    \nReason: {e}""".format(name=name, email=email, e=e))

    def print_catalog(self):
        """
        Print book titles and isbn number of each book in tome rater instance
        """
        for book in self.books.keys():
            print(book.get_title(), book.get_isbn())

    def print_users(self):
        """
        Print user name and email of each user in tome rater instance
        """
        for user in self.users.values():
            print(user.name, user.email)

    def most_read_book(self):
        """
        Returning a array intead of single book as per project requirement
        Array is for case if the most read book is a tie between multiple books
        """
        if len(self.books)> 0:
            books = list(self.books.items())
            books.sort(key = lambda x:x[1], reverse = True)
            most_read_book=[(book.title, reads) for book, reads in books if reads==books[0][1]]
        return most_read_book

    def highest_rated_book(self):
        """
        Return the book title that has the highest average rating
        In case of tie will return all book title with highest rating
        """
        rating_book = [(book, book.get_average_rating()) for book in self.books.keys()]
        rating_book.sort(key = lambda x:x[1], reverse = True)
        max_rating_book = [(book.title, avg_rating) for book, avg_rating in rating_book if avg_rating == rating_book[0][1]]
        return max_rating_book

    def most_positive_user(self):
        """
        Return the user name that has the highest average rating
        In case of tie will return all user names with highest rating
        """
        avg_rating_user = [(user, user.get_average_rating()) for user in self.users.values()]
        avg_rating_user.sort(key = lambda x:x[1], reverse = True)
        positive_users = [(user.name, avg_rating) for user, avg_rating in avg_rating_user if avg_rating == avg_rating_user[0][1]]
        return positive_users


    def get_n_most_read_books(self, n):
        """
        Returns first n most read books
        Print a human readable message if there are no books in the instance of tome rater
        """
        if type(n)==int:
            if len(self.books)  > 0 :
                n = len(self.books) if n > len(self.books) else n
                book_list = [(book.title, no_of_reads) for book, no_of_reads in self.books.items()]
                book_list.sort(key = lambda x:x[1], reverse = True)
                n_most_read_books=book_list[:n]
            else:
                print("No books available to list")
            return n_most_read_books
        else:
            print("Wrong argument type n = {n}".format(n=n))

    def get_n_most_prolific_readers(self, n):
        if type(n) == int:
            user_reads = [(user.name, user.no_of_books_read()) for user in self.users.values()]
            user_reads.sort(key=lambda x:x[1], reverse = True)
            most_prolific_users = user_reads[:n]
            return most_prolific_users
        else:
            print("Wrong argument type n = {n}".format(n=n))

    def get_n_most_expensive_books(self, n):
        """
        Return the top n books with highest price
        """
        if type(n) == int:
            book_price = [(book, book.get_price()) for book in self.books.keys()]
            book_price.sort(key=lambda x:x[1], reverse = True)
            return book_price[:n]
        else:
            print("Wrong argument type n = {n}".format(n=n))

    def get_worth_of_user(self, user_email):
        """
        Return the sum of the price of all the books read
        """
        price_list = [book.price for book in self.users.get(user_email).books.keys()]
        return sum(price_list)
