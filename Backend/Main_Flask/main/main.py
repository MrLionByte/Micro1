from dataclasses import dataclass
# from msilib.schema import PublishComponent
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
import requests
# from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id','product_id', name='user_product_unique')

@app.route('/api/products', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(Product.query.all())
    elif request.method == 'POST':
        data = request.get_json()
        new_product = Product(**data)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product created!"}), 201


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    json = req.json()

    try:
        user_id = json['id']
        existing_like = ProductUser.query.filter_by(user_id=user_id, product_id=id).first()
        if existing_like:
            return jsonify({
                'message': 'You already liked this product'
            }), 400

        product_user = ProductUser(user_id=user_id, product_id=id)
        db.session.add(product_user)
        db.session.commit()

        # PublishComponent('product_liked', id)
        
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        abort(400, 'An error occurred')

    return jsonify({
        'message': 'success'
    })
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

