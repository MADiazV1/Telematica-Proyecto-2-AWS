from flask import Blueprint, request, redirect, url_for, jsonify
from models.purchase import Purchase
from models.book import Book
from extensions import db
from functools import wraps
import jwt

purchase = Blueprint('purchase', __name__)
SECRET_KEY = 'secretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message': 'Token missing'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user_id = data['id']
        except Exception as e:
            return jsonify({'message': 'Token invalid'}), 401

        return f(current_user_id, *args, **kwargs)
    return decorated

@purchase.route('/buy/<int:book_id>', methods=['POST'])
@token_required
def buy(current_user_id, book_id):
    quantity = int(request.form.get('quantity'))
    price = float(request.form.get('price'))

    book = Book.query.get_or_404(book_id)

    if book.stock < quantity:
        return "No hay suficiente stock disponible.", 400

    total_price = price * quantity

    new_purchase = Purchase(
        user_id=current_user_id,
        book_id=book_id,
        quantity=quantity,
        total_price=total_price,
        status='Pending Payment'
    )
    book.stock -= quantity
    db.session.add(new_purchase)
    db.session.commit()

    return redirect(url_for('payment.payment_page', purchase_id=new_purchase.id))
