

import pika
import random
import time

print("# ---- SUBSCRIBER ---- #")

# connect
parameters = pika.ConnectionParameters(
    host='localhost',
    port=32775
)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# create a queue
channel.queue_declare(queue='hello')

def handle_consume(ch, method, properties, body):
    print(f"Received: {body}")

# transaction
channel.basic_consume(
    'hello',
    auto_ack=True,
    on_message_callback=handle_consume
)
channel.start_consuming()

connection.close()
