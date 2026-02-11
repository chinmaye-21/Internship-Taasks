class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # User-friendly representation
    def __str__(self):
        return f"'{self.title}' by {self.author} costs ₹{self.price}"

    # Developer-friendly representation
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"


# Creating two objects
book1 = Book("Python Basics", "John Smith", 499)
book2 = Book("Data Science Guide", "Emma Brown", 799)

# Printing using print()
print(book1)
print(book2)

# Printing inside a list
print([book1, book2])
