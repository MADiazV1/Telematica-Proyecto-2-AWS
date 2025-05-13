from flask import Flask
from extensions import db
from controllers.purchase_controller import purchase
from controllers.payment_controller import payment
from controllers.delivery_controller import delivery

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'  # Este valor debe ser igual al usado para generar el JWT en auth-service
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://order_user:order_pass@db_order/orderdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)

# Registrar blueprints
app.register_blueprint(purchase, url_prefix='/orders')
app.register_blueprint(payment, url_prefix='/payments')
app.register_blueprint(delivery, url_prefix='/deliveries')

@app.route('/')
def index():
    return '<h1>Order Service running</h1>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5002, debug=True)
