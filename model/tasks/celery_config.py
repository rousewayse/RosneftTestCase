from os import environ



environ.setdefault('BROKER_URL', 'pyamqp://localhost/')
environ.setdefault('RESULT_URL', 'redis://localhost:6379/')

broker_url = environ.get('BROKER_URL')
result_backend = environ.get('RESULT_URL')

#Results never expire
result_expires = 0

#Queues
task_create_missing_queues = True
default_queue = 'default'

#Serialization 
accept_content = ['application/json']
result_accept_content = ['application/json']

#time limits
task_time_limit = 10
task_soft_time_limit = 10

task_reject_on_worker_lost = True
