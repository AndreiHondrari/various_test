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
        print(f"SENDING: \"{message}\"")
        res = app.send_task('bla.some', (message,))
        print(res.id)

        res2 = AsyncResult(id=res.id, app=app)
        print(f"RES STATE: {res2.state}")

        count = 0
        forcres = None
        while res2.state == states.PENDING:
            print("RES STATE PENDING. RETRYING ...")
            time.sleep(0.25)
            count += 1
            if count == 5:
                forcres = res2.get(timeout=1)
                print(f"FORCED RES {forcres}")
                break

        if forcres is None:
            print(f"RESULT {res.get()}")

        time.sleep(1)
except KeyboardInterrupt:
    print("Warm interrupt of the sender")
