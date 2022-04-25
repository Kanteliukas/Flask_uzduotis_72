from py_client import ShoppingBasket

product = ShoppingBasket.add_product(product_name="pienas", price=2.09, quantity=1)
product["price"] = 1.69
product = ShoppingBasket.update_product_information(**product)
print(product)
