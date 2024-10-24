from app.models import db


class Carts(db.Model):
    id_cart: int = db.Column(db.Integer, primary_key=True)
    product_id: int = db.Column(db.Integer, db.ForeignKey('products.id_product'), nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)

    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity

