from .db import db
from pony import orm

class Sessions(db.Entity):
    _table_ = 'sessions'
    id = orm.PrimaryKey(int, auto=True)
    task_id = orm.Required(str, nullable=False, unique=True)

