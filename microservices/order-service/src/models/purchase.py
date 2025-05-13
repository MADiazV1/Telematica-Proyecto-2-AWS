from extensions import db

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    payments = db.relationship('Payment', backref='purchase', lazy=True)
    delivery_assignment = db.relationship('DeliveryAssignment', backref='purchase', uselist=False)

    def __repr__(self):
        return f'<Purchase book_id={self.book_id} user_id={self.user_id} status={self.status}>'
