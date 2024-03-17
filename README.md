
# About solution
The solution consists of 5 entities:

- `rabbitMQ`
- `redis`
- `celery`
- `fastapi`
- `PostgresSQL`

`FastAPI` is a entrypoint to whole service. It receives user's requests, creates task's for  `Celery` by queueing them into `rabbitMQ`. Then `Celery` worker executes this tasks. Results of finished tasks is stored in `Redis`. Finally, `FastAPI` takes results and gives it to user.   

There're two ways of computing sum: syncronous and asyncronous. That's why two different route controller are implemented:

- `/sync/` for syncronous computation
- `/async` for asyncronous computation

## How computation works:
### Syncronous
User makes post request to a `/sync/sum` route and API responses with result.  While computation is in progress (it may be pending or processing) http connection stays opened and unicorn proces with event loop is blocked. Waiting for task result is  blocking operation. If computation takes a long time (and only one unicorn process is available), api services may seem to be dead. I've tried to solve this problem but failed :(  

### Asyncronous
User post a task to `/async/post_task` route and gets a session id value. This value is needed for getting a task execution results by making a GET request to `/async/get_task_result`. If `null` is returned, it means that task in not finished yet. 

Ayncronous manner is the reason why `Celery` is used. `PostgresSQL` is needed to store session ids. 

## Documentation
You're free to check auto-generated `OpenAPI` docs by looking at `/docs`. 


## Deploying
For an easier deployment [docker-compose.yml](./docker-compose.yml) is written. All you need is to run in terminal (maybe root permissions are required, by default api binds to  `80` port):
```
docker-compose up --build -d 
```
Don't like Docker? You can run all services by yourself with additional configuration (Export some environment variables). Look at configs:

- For [PonyORM](./model/db/pony_cfg.py)
- For [Celery](./model/tasks/celery_config.py)

Happy configuring then...

Only Database is required to get an api running (for startup). If connections break suddenly, api should return `500` HTTP error and describe what's wrong. Try:
```
docker-compose stop postres
#or
docker-compose stop rabbit
#or
docker-compose stop redis
#or
docker-compose stop celery 
```

### Database population?
You don't need it. PonyORM automaticly creates tables when module `model` is imported. 
