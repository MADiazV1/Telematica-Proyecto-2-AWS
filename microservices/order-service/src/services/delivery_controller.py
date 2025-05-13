from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.delivery import DeliveryProvider
from models.delivery_assignment import DeliveryAssignment
from extensions import db
from functools import wraps
import jwt

delivery = Blueprint('delivery', __name__)
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

@delivery.route('/delivery/<int:purchase_id>', methods=['GET', 'POST'])
@token_required
def select_delivery(current_user_id, purchase_id):
    providers = DeliveryProvider.query.all()
    if request.method == 'POST':
        selected_provider_id = request.form.get('provider')
        new_assignment = DeliveryAssignment(purchase_id=purchase_id, provider_id=selected_provider_id)
        db.session.add(new_assignment)
        db.session.commit()
        return redirect(url_for('book.catalog'))  # Verifica que esta ruta exista
    return render_template('delivery_options.html', providers=providers, purchase_id=purchase_id)
