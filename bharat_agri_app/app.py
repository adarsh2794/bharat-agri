from flask import Flask
from celery import Celery
import uuid

app = Flask(__name__)
agri_app = Celery('background_worker_thread', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.route('/agri/pay')
def pay_method():
    app.logger.info("Initiating Payment")
    r = agri_app.send_task('tasks.takePaymentRequest', kwargs={'user': "User " + str(uuid.uuid1())})
    app.logger.info(r.backend)
    return r.id


@app.route('/agri/pay/status/<payment_id>')
def get_pay_status(payment_id):
    status = agri_app.AsyncResult(payment_id, app=agri_app)
    print("Checking Payment status")
    return "Status of the Task " + str(status.state)


@app.route('/agri/pay/result/<payment_id>')
def task_result(payment_id):
    result = agri_app.AsyncResult(payment_id).result
    return "Result of the Task " + str(result)
