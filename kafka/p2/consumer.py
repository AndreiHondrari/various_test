import random

from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers="localhost:9092")


print("--- Kafka Consumer (replay from 0) ---\n")

# acquire topics
topics = list(consumer.topics())

topics_print = '\n'.join(topics)
print(f"Subscribing to following topics: {topics_print}")

# subscribe to topics
for topic in topics:
    consumer.subscribe(topic)

# !!! Get assignments and define partitions
print("Get assignments ...")
for topic in topics:
    consumer.partitions_for_topic(topic)

assignments = consumer.assignment()
assignments_print = '\n'.join([f"{tp.topic}: {tp.partition}" for tp in assignments])
print(f"Assignments: {assignments_print}")

# rollback
print("Rollback to 0 all topics")
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
