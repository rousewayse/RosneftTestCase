from fastapi import FastAPI, Body, Depends, HTTPException, Header, APIRouter, Query
import model
from model.exceptions import CeleryNotWorkingException, PonyNotWorkingException, TaskNotFoundException
from typing import Union, List, Annotated, Dict
from ..models import InputData, check_content_type, common_request_body, CommonDep 

sync_router = APIRouter(
        prefix='/sync',
        tags=['Syncronous method'],
        dependencies=[Depends(check_content_type)]
        )

@sync_router.post('/sync/sum',
          description="Perform a sum calculation of some numbers array",
          response_description="Calculated sum",
          ) 
def perform_sync(args: CommonDep)->Dict:
    try:
        return {'result': model.sum_sync(args.args)}
    except CeleryNotWorkingException as e:
        raise HTTPException(500, e.message)


