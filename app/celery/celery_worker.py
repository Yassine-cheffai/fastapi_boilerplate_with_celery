import os
import time
from celery import Celery


CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER_URL")
CELERY_BROKER_URL = os.environ.get("CELERY_RESULT_BACKEND")
if not CELERY_BROKER_URL or not CELERY_RESULT_BACKEND:
    print("issues with the celery env variables")

celery = Celery(__name__)

celery.conf.broker_url = CELERY_BROKER_URL
celery.conf.result_backend = CELERY_RESULT_BACKEND


@celery.task(name="create_task")
def create_task(delay_amount, x, y):
    time.sleep(delay_amount)
    return x + y
