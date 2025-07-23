from abc import ABC, abstractmethod
class Cart(ABC):
    @abstractmethod
    def add_to_cart(self, product_name, quantity):
        pass
class ShoppingCart(Cart):
    def __init__(self):
        self.products = {
            "Sugar": 50,

            "Rice": 55,
            "Wheat flour": 55,
            "Toor dal": 150,
            "Rava": 70
        }
        self.cart = {}

    def display_products(self):
        print("Product: Price in Rs.")
        for product, price in self.products.items():
            print(f"{product}: {price}")
    def add_to_cart(self, product_name, quantity):
        if product_name in self.products:
            if quantity > 0:
                total_price = self.products[product_name] * quantity
                self.cart[product_name] = (quantity, total_price)
                print("Cart:")
                print("Product: Quantity: Price in Rs.")
                for item, details in self.cart.items():
                    print(f"{item}: {details[0]}: {details[1]}")
                print("Thank you")
            else:
                print("Thank you")
        else:
            print("Please enter the existing product's name in the list")
def main():
    shopping_cart = ShoppingCart()
    shopping_cart.display_products()

    product_name = input("Enter the item name to add it to the cart:")
    if product_name in shopping_cart.products:
        try:
            quantity = int(input("Enter the quantity in Kgs:"))
            shopping_cart.add_to_cart(product_name, quantity)
        except ValueError:
            print("Please enter a valid number for quantity.")
    else:
        print("Please enter the existing product's name in the list")
main()
