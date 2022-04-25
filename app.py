from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'shopping_basket.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Product(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "product_name", "price", "quantity")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route("/product", methods=["POST"])
def add_product():
    db.create_all()
    product_name = request.json["product_name"]
    price = request.json["price"]
    quantity = request.json["quantity"]
    new_product = Product(product_name=product_name, price=price, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

@app.route("/product", methods=["GET"])
def get_all_products():
    
    products = Product.query.all()
    result = products_schema.dump(products)
    return jsonify(result)

@app.route("/product/<id>", methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

@app.route("/product/<id>", methods=["PUT"])
def update_product_information(id):
    product = Product.query.get(id)
    product.product_name = request.json["product_name"]
    product.price = request.json["price"]
    product.quantity = request.json["quantity"]
    db.session.commit()
    return product_schema.jsonify(product)

@app.route("/product/<id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return product_schema.jsonify(product)
    else:
        return f"Error: product with id {id} not found!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()