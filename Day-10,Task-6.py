
class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    # Access item by index
    def __getitem__(self, index):
        return self.items[index]

    # Update item by index
    def __setitem__(self, index, value):
        self.items[index] = value


# Creating a shopping cart with initial items
cart = ShoppingCart(["Apple", "Banana", "Orange"])

# Accessing items
print(cart[0])  # Output: Apple

# Updating an item
cart[1] = "Mango"

# Checking updated list
print(cart.items)  # Output: ['Apple', 'Mango', 'Orange']

