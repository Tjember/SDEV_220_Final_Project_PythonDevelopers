
class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        if product.product_id not in self.inventory:
            self.inventory[product.product_id] = product
        else:
            print(f"Product with ID {product.product_id} already exists in the inventory.")

    def remove_product(self, product_id):
        if product_id in self.inventory:
            del self.inventory[product_id]
        else:
            print(f"Product with ID {product_id} not found in the inventory.")
            
class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        return f"Product ID: {self.product_id}", f"Product Name: {self.name}", f"Description: {self.description}", f"Price: ${self.price:.2f}",f"Quantity: {self.quantity}"
    
    def update_quantity(self, quantity_change):
        self.quantity += quantity_change