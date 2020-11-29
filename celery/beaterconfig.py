broker_url = "amqp://guest:guest@localhost:5672"
result_backend = 'rpc://'
task_default_queue = "test_queue"
beat_schedule = {
    'some-beater': {
        'task': 'beater.some',
        'schedule': 5.0
    }
}
