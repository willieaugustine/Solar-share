from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solar_share.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tokens = db.Column(db.Integer, default=0)

db.create_all()

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        data = request.json
        user = User(username=data['username'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Profile created'}), 201
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    return jsonify({'username': user.username, 'tokens': user.tokens} if user else 'User not found')

@app.route('/trade', methods=['POST'])
def trade():
    data = request.json
    sender = User.query.filter_by(username=data['sender']).first()
    receiver = User.query.filter_by(username=data['receiver']).first()
    amount = data['amount']
    if sender and receiver and sender.tokens >= amount:
        sender.tokens -= amount
        receiver.tokens += amount
        db.session.commit()
        return jsonify({'message': 'Trade successful'})
    return jsonify({'message': 'Insufficient tokens'}), 400

if __name__ == '__main__':
    app.run(debug=True)
