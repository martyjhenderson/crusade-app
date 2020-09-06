from app import app, db
from app.models import User, OrderOfBattle, Units, BattleLog

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'oob': OrderOfBattle, 'Units': Units, 'log': BattleLog}