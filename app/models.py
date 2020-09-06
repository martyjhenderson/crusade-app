from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class OrderOfBattle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    player = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<OrderOfBattle %r>' % self.name

class Units(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    oob = db.Column(db.Integer, db.ForeignKey('order_of_battle.id'))

    def __repr__(self):
        return '<Units %r>' % self.name

class BattleLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    attacker = db.Column(db.String(80), nullable=True)
    defender = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<BattleLog %r>' % self.name