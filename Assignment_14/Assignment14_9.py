class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if (other, Product):
            return self.price == other.price
        return False

# Example usage
product1 = Product("Laptop", 1000)
product2 = Product("Phone", 1000)
product3 = Product("Tablet", 800)

print(product1 == product2)  # True (prices are equal)
print(product1 == product3)  # False (prices are different)
