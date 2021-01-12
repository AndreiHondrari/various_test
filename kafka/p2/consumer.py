import random
import time

from kafka import KafkaConsumer
from tenacity import Retrying, stop_after_attempt, wait_fixed, RetryError

consumer = KafkaConsumer(bootstrap_servers="localhost:9092")


print("--- Kafka Consumer (replay from 0) ---\n")

# acquire topics
topics = list(consumer.topics())
consumer.poll(0)

topics_print = '\n'.join([f"\t{t}" for t in topics])
print(f"Subscribing to following topics:\n{topics_print}")

# subscribe to topics
consumer.subscribe(topics)
consumer.topics()  # force assignment

# !!! Get assignments and define partitions
print("\nGet assignments ...")
assignments = None

try:
    for attempt in Retrying(wait=wait_fixed(3), stop=stop_after_attempt(3)):
        with attempt:
            assignments = consumer.assignment()
            print(f"Current assignments: {assignments}")
            if len(assignments) == 0:
                raise Exception

except RetryError:
    print("Could not obtain topic assignment. Exiting ...")
    exit(1)

assignments_print = '\n'.join([f"\t{tp.topic}: {tp.partition}" for tp in assignments])
print(f"\nAssignments:\n{assignments_print}")

# rollback
print("\nRollback to 0 all topics")
for topic_partition in assignments:
    consumer.seek(topic_partition, 0)  # put from beginning

print("Start listening ...")
try:

    while 1:
        record = next(consumer)
        value = record.value.decode()
        print(f"{record.topic}: {value}")

except KeyboardInterrupt:
    print("gracefully closing consumer")
    consumer.close()
