from book import Book
"""
Create User object
"""
class User(object):
    def __init__(self, name, email):
        try:
            if name == "":
                raise Exception("Invalid name: Empty string")
            self.name = name
            if not self.email_check(email=email):
                raise Exception("Invalid email format: {email}".format(email=email))
            self.email = email
            self.books = {}
        except Exception as e:
            print("Failed to intialize user.\nReason : {e}".format(e=e))

    """
    Dunder methods for User class
    """
    def __repr__(self):
        books_read = len(self.books)
        return "User {}, email: {}, books read :{}".format(self.name, self.email, books_read)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    """
    class methods
    """
    def email_check(self, email):
        """
        Check if '@' exists in email
        Check if '.com', '.edu', '.org' exists as extension.
        Extension check logic is list based so any other extensions can easily be added to list
        """
        valid_exts = ['.com', '.edu', '.org']
        if len([ext for ext in valid_exts if ext in email])> 0 and '@' in email:
            return True
        else:
            return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        """
        Check new email format
        Human readable message is printed for success or failure of method
        """
        try:
            if not email_check(email=email):
                raise Exception("Invalid email format: {email}".format(email=email))
            self.email = address
            print("{} user's email is updated successfully,\nUpdated email : {}".format(self.name, self.email))
        except Exception as e:
            print("failed to update email for user : {name}\nReason: {e}".format(name=self.name,e=e))

    def read_book(self, book, rating=None):
        """
        Check if the book arguemet supplied is a valid book type
        Adding book object name with rating between 0 to 4  to the array
        Human readable message is printed if the value is not None and not beteen 0 and 4
        Add book with None rating
        """
        if isinstance(book, Book):
            if not rating == None:
                if 0<= rating <= 4:
                    self.books.update({book: rating})
                else:
                    print("Invalid Rating :{}".format(rating))
            else:
                self.books.update({book: rating})
        else:
            print("{} object is not valid Book type! rating is not added".format(book))

    def get_average_rating(self):
        """
        Returns the average rating for books with a rating.
        books with None rating will be ignored.
        If there are no books, or all ratings are None, then -1 will be returned.
        """
        ratings = [rating for rating in self.books.values() if not rating==None]
        if len(ratings) > 0:
            return sum(ratings)/len(ratings)
        else:
            return -1

    def no_of_books_read(self):
        """
        Returns the number of books read by the User
        """
        return len(self.books)
