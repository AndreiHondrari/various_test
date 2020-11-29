# How to use this celery example

## Consumer

In order to start the worker with the task run the command:

`celery -A consumer worker`

## Sender

In order to start using the remove worker at the other end of the message queue:

`python sender.py`
