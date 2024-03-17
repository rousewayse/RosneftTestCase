from fastapi import FastAPI, Body, Depends, HTTPException, Header, APIRouter, Query
import model
from model.exceptions import CeleryNotWorkingException, PonyNotWorkingException, TaskNotFoundException
from typing import Union, List, Annotated, Dict
from ..models import InputData, check_content_type, common_request_body, CommonDep 
async_router = APIRouter(
        prefix='/async',
        tags=['Asyncronous method'],
        )

@async_router.post('/async/post_task',
          description='Post a new task for async task computation',
          response_description='Session id',
          dependencies=[Depends(check_content_type)]
          )
def post_task(args: CommonDep)->Dict:
    try:
        session_id = model.create_task(args.args)
        return {'session_id': session_id}
    except (CeleryNotWorkingException, PonyNotWorkingException) as e:
        raise HTTPException(500, e.message)

@async_router.get('/async/get_task_result',
         description= 'Get result of task computation via it\'s session id',
         response_description='Calculated sum'
         )
def get_task(session_id: Annotated[int, Query(gt=0, title='Session id', description='A session id that is received form posting task route')])->Dict:
    try:
        result = model.get_task(session_id)
        return {'result': result}
    except TaskNotFoundException as e: 
        raise HTTPException(400, e.message)
    except (CeleryNotWorkingException, PonyNotWorkingException) as e:
        raise HTTPException(500, e.message)


