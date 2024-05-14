# task 1

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author
        
    def read(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        
book1 = Book("Harry Potteer", 23.99, 4, "J.K Rowling")

book1.read()

# task 2

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu
        
class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
        
    def order(self, name, quantity_ordered):
        dish_description = self.menu.get(name)
        if dish_description is None:
            return 'Dish not available'
        quantity_in_stock = dish_description['quantity']
        if quantity_in_stock == 0 or quantity_in_stock < quantity_ordered:
            return 'Requested quantity not available'

        dish_description['quantity'] = quantity_in_stock - quantity_ordered
        
        return str(quantity_ordered * dish_description['price'])
    
    
menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available