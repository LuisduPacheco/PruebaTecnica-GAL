from app.models import db


class Products(db.Model):
    id_product: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(45), nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity
