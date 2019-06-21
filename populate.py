from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
#modified to add price as an argument
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 9.99)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", 12345, 5.99, "Lewis Carroll")
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", 1929452, 10.99, "Python", "beginner")
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", 11111938, 11.99, "AI", "advanced")
novel2 = Tome_Rater.create_novel("The Diamond Age", 10101010, 5.99, "Neal Stephenson")
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", 10001000, 7, "Ray Bradbury")

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com")
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 2)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 3)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 3)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print("\nPrinting Catalog:")
Tome_Rater.print_catalog()
print("\nPrinting Users:")
Tome_Rater.print_users()
print("\nMost positive user:")
print(Tome_Rater.most_positive_user())
print("\nHighest rated book:")
print(Tome_Rater.highest_rated_book())
print("\nMost read book:")
print(Tome_Rater.most_read_book())
print("\nFirst n most read book:")
print(Tome_Rater.get_n_most_read_books(3))
print("\nFirst n most prolific users:")
print(Tome_Rater.get_n_most_prolific_readers(2))
print("\nFirst n most expensive books:")
print(Tome_Rater.get_n_most_expensive_books(3))
print("\nSum of cost of books read by user:")
print(Tome_Rater.get_worth_of_user("marvin@mit.edu"))
print("\nTest add user with bad format:")

#Create users with bad email format:
Tome_Rater.add_user("John Doe", "jdoe@turing.mock")
Tome_Rater.add_user("John Doe", "jdoe.com")
Tome_Rater.add_user("", "jdoe@turing.com")

#lets add book with same isbn
print("\nTest book with duplicate isbn")
novel4 = Tome_Rater.create_novel("Mock Novel 3", 10001000, 10.99, "Ray Bradbury")
