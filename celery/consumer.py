import random
import time

from celery import Celery

app = Celery('bla')
app.config_from_object('celeryconfig')

print("---- CONSUMER ----")


@app.task(name='bla.some')
def some(msg):
    # input section
    print(msg)

    # processing section
    print("Process for a bit ...")
    time.sleep(random.random())

    # result section
    result = random.randint(0, 100)
    print(f"Return result {result}")
    return result


print(f"task {some.name}")
