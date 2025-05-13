from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.payment import Payment
from models.purchase import Purchase
from extensions import db
from functools import wraps
import jwt

payment = Blueprint('payment', __name__)
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

@payment.route('/payment/<int:purchase_id>', methods=['GET', 'POST'])
@token_required
def payment_page(current_user_id, purchase_id):
    if request.method == 'POST':
        method = request.form.get('method')
        amount = request.form.get('amount')

        new_payment = Payment(
            purchase_id=purchase_id,
            amount=amount,
            payment_method=method,
            payment_status='Paid'
        )
        db.session.add(new_payment)

        purchase = Purchase.query.get(purchase_id)
        purchase.status = 'Paid'
        db.session.commit()

        return redirect(url_for('delivery.select_delivery', purchase_id=purchase_id))
    
    return render_template('payment.html', purchase_id=purchase_id)
