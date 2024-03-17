from . import tasks
from .db import db, entities
from pony import orm
from celery.result import AsyncResult
from typing import Union, List
from .exceptions import *
def sum_sync(args: List[Union[float, int]])->Union[float, int]:
    try: 
        result = tasks.task.add.delay(args).get()
        return result
    except Exception as e:
        raise CeleryNotWorkingException("seems like celery consumer has some troubles :)")

def create_task(args: List[Union[float, int]])->int:
    try:
        task_id = tasks.task.add.delay(args).task_id
    except Exception as e: 
        raise CeleryNotWorkingException("seems like celery consumer has some troubles :)")

    new_session = None
    with orm.db_session:
        try: 
            new_session = entities.Sessions(task_id=task_id)
            new_session.flush()
        except Exception as e:
            raise PonyNotWorkingException('seems like PonyORM experienced some troubles :(')
            
    return new_session.id


def get_task(session_id: int)->Union[int, float, None]:
    from .tasks import app
    session = None
    with orm.db_session:
        try:
            session = entities.Sessions.get(id=session_id)
        except Exception as e:
            raise PonyNotWorkingException('seems like PonyORM experienced some troubles :(')

        if session is None:
            raise TaskNotFoundException(f'Task with given id {session_id} does not exist')
        try:
            task = app.AsyncResult(session.task_id)
            if task.ready():
                #session.delete()
                return task.get()
        except Exception as e:
            raise CeleryNotWorkingException('seems like celery consumer has some troubles :)')
    return None

