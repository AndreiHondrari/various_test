import random
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")


print("--- Kafka Producer ---\n")

print("Start sending ...")
try:
    while 1:
        message = f"Hello {random.randint(0, 100)}"
        print(f"Sending {message}")
        producer.send('topic1', message.encode())
        time.sleep(1.5)

except KeyboardInterrupt:
    print("gracefully closing producer")
    producer.close()
