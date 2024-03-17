from fastapi import FastAPI
from .routes import sync_route, async_route
description ='''
You\'re able to calculate sum in two manners:
- Syncronous
- Asyncronous
        
See apropriate tags and endpoints
'''
openapi_tags = [
        {'name': 'Syncronous method', 'description' : 'Perform sum calculation whithin a single request'},
        {'name': 'Asyncronous method', 'description': 'Perform sum calculation in asyncronous manner: post new task and then request results later'}
        ]
       

app = FastAPI(
        title = 'Test case service for doing some math',
        description = description,
        openapi_tags = openapi_tags
        ) 
app.include_router(sync_route.sync_router)
app.include_router(async_route.async_router)


