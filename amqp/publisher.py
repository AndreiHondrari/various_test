
import pika
import random
import time

print("# ---- PUBLISHER ---- #")

# connect
parameters = pika.ConnectionParameters(
    host='localhost',
    port=32775
)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# create a queue
channel.queue_declare(queue='hello')

# transactions
print("Start sending ...")
try:
    while 1:
        message = f"Hello {random.randint(0, 100)}"
        print(f"Sending {message}")
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body=message
        )
        time.sleep(3)

except KeyboardInterrupt:
    print("gracefully closing publisher")

connection.close()
