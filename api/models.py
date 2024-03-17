from fastapi import FastAPI, Body, Depends, HTTPException, Header, APIRouter, Query
from typing import Union, List, Annotated, Dict
from pydantic import BaseModel, Field

class InputData(BaseModel):
    args: List[Union[int, float]] = Field(
            default=None,
            title="Array of items to sum",
            description='Array of numbers to sum'
            )
    model_config = {
            'json_schema_extra': {
                    'examples':[
                        {'args':[1, 2, 3, 4, 5]}, {'args': [1.0, 2.0, 3.0, 4.0]}
                    ]
                }
            }


def check_content_type(content_type: str = Header(default='application/json'))->None:
    if content_type != 'application/json':
        raise HTTPException(415, 'Only json request bodies are accepted')

def common_request_body(args: Annotated[InputData, Body(title='array of items to sum')]):
    return args
CommonDep = Annotated[dict, Depends(common_request_body)]


