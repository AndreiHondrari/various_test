import pika

# Create a global channel variable to hold our channel object in
channel = None

# Step #2
def on_connected(connection):
    """Called when we are fully connected to RabbitMQ"""
    print("Fully connected to RabbitMQ")
    # Open a channel
    connection.channel(on_open_callback=on_channel_open)

# Step #3
def on_channel_open(new_channel):
    """Called when our channel has opened"""
    global channel
    channel = new_channel
    channel.queue_declare(
        queue="hello",
        durable=True,
        exclusive=False,
        auto_delete=False,
        callback=on_queue_declared
    )

# Step #4
def on_queue_declared(frame):
    """Called when RabbitMQ has told us our Queue has been declared, frame is the response from RabbitMQ"""
    print("Consume")
    channel.basic_consume('hello', handle_delivery)

# Step #5
def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    print(body)

# Step #1: Connect to RabbitMQ using the default parameters
parameters = pika.ConnectionParameters(host='localhost', port=32775)
connection = pika.SelectConnection(parameters, on_open_callback=on_connected)

try:
    # Loop so we can communicate with RabbitMQ
    connection.ioloop.start()
except KeyboardInterrupt:
    # Gracefully close the connection
    connection.close()
    # Loop until we're fully closed, will stop on its own
    connection.ioloop.start()
