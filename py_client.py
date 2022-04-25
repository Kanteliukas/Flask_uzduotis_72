import requests
import json

class ShoppingBasket():
    @staticmethod
    def add_product(product_name: str, price: float, quantity: int) -> dict:
        new_product = {
            "product_name" : product_name,
            "price" : price,
            "quantity" : quantity
        }

        result = requests.post('http://127.0.0.1:8000/product', json=new_product)
        return result.json()

    @staticmethod
    def get_all_products() -> dict:
        results = requests.get('http://127.0.0.1:8000/product')
        return results.json()

    @staticmethod
    def get_product(id: int) -> dict:
        result = requests.get(f'http://127.0.0.1:8000/product/{id}')
        return result.json()

    @staticmethod
    def update_product_information(id: int, product_name: str, price: float, quantity: int) -> dict:    
        updated_product = {
            "product_name" : product_name,
            "price" : price,
            "quantity" : quantity
        }

        result = requests.put(f'http://127.0.0.1:8000/product/{id}', json=updated_product)
        return result.json()

    @staticmethod
    def delete_product(id: int) -> dict:
        result = requests.delete(f'http://127.0.0.1:8000/product/{id}')
        return result.json()