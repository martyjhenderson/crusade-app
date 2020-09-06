from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from sqlalchemy import MetaData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## In order to use SQLLite, you _must_ have metadata or else SQL Alchemy pukes
## Src: https://stackoverflow.com/a/46785675
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(app, metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate(app, db)

## Without this snippet, it appears that sqlite will always fail when there is an "Alter" statement in SQLAlchemy
## Src: https://stackoverflow.com/questions/30394222/why-flask-migrate-cannot-upgrade-when-drop-column/54322445#54322445
with app.app_context():
  if db.engine.url.drivername == 'sqlite':
    migrate.init_app(app, db, render_as_batch=True)
  else:
    migrate.init_app(app, db)


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class OrderOfBattle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    player = db.Column(db.Integer, db.ForeignKey('players.id'))

class Units(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    oob = db.Column(db.Integer, db.ForeignKey('order_of_battle.id'))

class BattleLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    attacker = db.Column(db.String(80), nullable=True)
    defender = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<BattleLog %r>' % self.name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        new_stuff = BattleLog(name=name)

        try:
            db.session.add(new_stuff)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new stuff."

    else:
        battles = BattleLog.query.order_by(BattleLog.created_at).all()
        return render_template('index.html', battles=battles)

@app.route('/delete/<int:id>')
def delete(id):
    battle = BattleLog.query.get_or_404(id)

    try:
        db.session.delete(battle)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting data."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    battle = BattleLog.query.get_or_404(id)

    if request.method == 'POST':
        battle.name = request.form['name']
        battle.attacker = request.form['attacker']
        battle.defender = request.form['defender']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating data."

    else:
        title = "Update Data"
        return render_template('update.html', title=title, battle=battle)


if __name__ == '__main__':
    app.run()
