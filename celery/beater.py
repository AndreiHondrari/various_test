from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('bla')
app.config_from_object('beaterconfig')

print("---- CONSUMER ----")


@app.task
def some():
    print("jump")
    logger.info("WHAZZAA")


print(f"task {some.name}")
