class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Equality comparison based on brand and model
    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False


# Creating three objects
mobile1 = Mobile("Samsung", "S23", 80000)
mobile2 = Mobile("Samsung", "S23", 82000)
mobile3 = Mobile("Apple", "iPhone 15", 90000)

# Comparing objects
print(mobile1 == mobile2)  # True (same brand and model)
print(mobile1 == mobile3)  # False (different brand and model)
