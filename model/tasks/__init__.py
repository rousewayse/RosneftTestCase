from celery import Celery

app = Celery(__name__)
app.config_from_object('model.tasks.celery_config')

from .import task

