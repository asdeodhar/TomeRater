class Book(object):
    def __init__(self, title, isbn, price):
        self.title= title
        self.isbn= isbn
        self.price= price
        self.ratings= []
    """
    Dunder methods for Book class
    """
    def __repr__(self):
        return "{title}".format(title=self.title)

    def __eq__(self, other_book):
        if isinstance(other_book, Book):
            return self.title == other_book.title and self.isbn == other_book.isbn
        else:
            print("objects are not of same type")

    def __hash__(self):
        """
        Creates a hash method for the Book object. This is used to have the Book
        instances used as keys in the books dictionary in the User object.
        """
        return hash((self.title, self.isbn))
    """
    class method
    """
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        try:
            self.isbn = new_isbn
        except:
            print("failed to update isbn number for book title:{}".format(self.title))

    def add_rating(self, rating):
        if not rating == None:
            if 0 <= rating <=4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating :{}".format(rating))

    def get_average_rating(self):
        if len(self.ratings) > 0:
            return sum(self.ratings)/len(self.ratings)
        else:
            return 0



class Fiction(Book):
    """
    The Fiction class inherits from Book
    """
    def __init__(self, title, isbn, price, author):
        super().__init__(title, isbn, price)
        self.author= author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author= self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    """
    The Non_Fiction class inherits from Book
    """
    def __init__(self, title, isbn, price, subject, level):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return " {title}, a {level} manual on {subject}".format(
            title= self.title,
            level= self.level,
            subject = self.subject
        )

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
