Bharat Agri Assignment

Question

Assignment:
1. Design a system to handle exponential backoff which can be used to poll or access
third-party APIs or resources with an irregular response or intermittent failures.
2. Recommended language and frameworks: Python, Flask/Django
3. Additional suggested resources: Celery, Redis, or other better alternatives
4. Example use case: A payment gateway integration might require such a system to
ensure that the payment status of pending payments is updated in due time.
5. You need to push your code to a VCS (Github etc.) and share the repository with
your response.
Tip: There can be just one (or a few) function(s) that can handle this. We’re primarily
interested in the approach and the logic in this function(s).
Recommended Time: 1 - 2 hours
   

Solution

In order to solve the above problem I have created a simple python application
using Flask 

To achieve exponential backoff I have created another application which are
worker threads

Workflow

1.The application (bharat_agri_app) will receive Payment Requests
using the API

    http://0.0.0.0:5000/agri/pay

2.This API will immediately push the task to the worker thread
and give back the payment id (<payment_id>)to the application 
by which the status of payment can be polled using the API

    http://0.0.0.0:5000/agri/pay/status/<payment_id>

3.As soon as the worker thread completes the execution it will push back the
result in the same redis from where it consumed the task

4.Once the result is pushed the status api will give a SUCCESS

5.In order to check the final result after SUCCESS user can hit the 
following API to get the result

    http://0.0.0.0:5000/agri/pay/result/<payment_id>

Note: In order to mock the random response timings of the 3rd party API's 
I have mocked that by adding a random sleep between (0,10) secs in worker threads

    n = random.randint(0, 10)
    logger.info("This worker will give response after " + str(n) + " seconds")
    time.sleep(n)

Note: I have dockerized the application which will have essentially 3 containers
1. Redis Container
2. Bharat Agri App Container
3. Background Worker Container

Docker will help to manage the dependencies using Docker Hub Images

Command to run the application from root directory(Bharat Agri)

    sudo docker-compose -f docker-compose.yml up




