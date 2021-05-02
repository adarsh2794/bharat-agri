import time
from celery import Celery
from celery.utils.log import get_task_logger
import random

logger = get_task_logger(__name__)

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.task()
def takePaymentRequest(user):
    logger.info('Got Payment Request from user' + user)
    # To mock random response times as per the given question
    n = random.randint(0, 10)
    logger.info("This worker will give response after " + str(n) + " seconds")
    time.sleep(n)
    return "Payment Success for " + user
