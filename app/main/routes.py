from flask import render_template, g
from flask import current_app as app
from . import main_bp
from ..models import Product, User


@main_bp.before_app_request
def load_user():
    from flask import session
    user_id = session.get('user_id')
    g.user = None
    if user_id:
        g.user = User.query.get(user_id)


@main_bp.route('/')
def index():
    products = Product.query.order_by(Product.created_at.desc()).limit(20).all()
    return render_template('index.html', products=products)
