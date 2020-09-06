from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, OrderOfBattle

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

class OrderOfBattleCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_orderofbattle(self):
        # create user
        u = User(username='testuser1', email='testuser1@crusade.test')
        db.session.add(u)
        # create an Order of Battle

        oob1 = OrderOfBattle(name='oobtest1', player=1)
        db.session.add(oob1)
        db.session.commit()

        self.assertEqual(oob1.player, u.id)

if __name__ == '__main__':
    unittest.main(verbosity=2)