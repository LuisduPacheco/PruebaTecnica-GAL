from app.models import db


class Shopping(db.Model):
    id_shopping = db.Column(db.Integer, primary_key=True)
    id_cart = db.Column(db.Integer, db.ForeignKey('carts.id_cart'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id_product'), nullable=False)