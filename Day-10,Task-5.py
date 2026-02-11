class Calculator:
    
    # Making the object callable
    def __call__(self, a, b):
        return a + b


# Creating object
obj = Calculator()

# Calling object like a function
print(obj(10, 20))
