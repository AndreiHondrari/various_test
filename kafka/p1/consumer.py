import random

from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers="localhost:9092")


print("--- Kafka Consumer ---\n")

# acquire topics
topics = list(consumer.topics())

topics_print = '\n'.join(topics)
print(f"Subscribing to following topics: {topics_print}")

# subscribe to topics
for topic in topics:
    consumer.subscribe(topic)

print("Start listening ...")
try:

    while 1:
        record = next(consumer)
        value = record.value.decode()
        print(f"{record.topic}: {value}")

except KeyboardInterrupt:
    print("gracefully closing consumer")
    consumer.close()
