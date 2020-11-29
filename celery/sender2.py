import random
import time

from celery import Celery, states
from celery.result import AsyncResult

app = Celery()
app.config_from_object('celeryconfig')

MESSAGES = [
    'Stefan pusca capreoara',
    'Alex trage firu',
    'Flo ne spune buna dimineata',
    'Mitza flexeaza muschiul',
    'Geo tureaza Bavarian Motor Works',
]

print("---- SENDER ----")

try:
    while True:
        message = random.sample(MESSAGES, 1)[0]

        print(f"Sending: \"{message}\"")
        response = app.send_task('bla.some', (message,))

        # what is the id
        print(f"Task ID: {response.id}")

        response = AsyncResult(id=response.id, app=app)

        for i in range(5):
            if response.ready():
                result = response.get(timeout=1)
                print(f"Result is {result}")
                break

            time.sleep(0.5)

        time.sleep(1)
except KeyboardInterrupt:
    print("Warm interrupt of the sender")
