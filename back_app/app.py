from celery import Celery

from back_app.config import celery_config


app = Celery(
    celery_config.APP_NAME,
    broker=celery_config.BROKER_URL
)