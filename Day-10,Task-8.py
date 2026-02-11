class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    # Check if an item exists in the books list
    def __contains__(self, item):
        return item in self.books


# Creating a library with some books
library = Library(["Python", "Java", "C++"])

# Checking if a book exists
print("Python" in library)  # True
print("Ruby" in library)    # False
