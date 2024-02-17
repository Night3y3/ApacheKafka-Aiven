import json
import time
import random
from kafka import KafkaProducer
from id import generate_unique_id
from fake import get_fake_pizza, get_fake_name, get_fake_address, get_fake_email, get_fake_phone

folderName = "./"
producer = KafkaProducer(
    # <INSTANCE_NAME>-<PROJECT_NAME>.aivencloud.com:<PORT>
    bootstrap_servers='kafka-demo-sabrexghosh-b0a4.a.aivencloud.com:19722',
    security_protocol="SSL",
    ssl_cafile=folderName + "ca.pem",
    ssl_certfile=folderName + "service.cert",
    ssl_keyfile=folderName + "service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)

# Initialize time for measuring the gap
last_send_time = time.time()

while True:
    order_id = generate_unique_id()  # Function to generate a unique ID
    pizza_type = get_fake_pizza() # Function to generate a random pizza type
    customer_name = get_fake_name() # Function to generate a random name
    customer_address = get_fake_address() # Function to generate a random address
    customer_email = get_fake_email() # Function to generate a random email
    customer_phone = get_fake_phone() # Function to generate a random phone number
    message_key = {"order_id": order_id}
    message_value = {"order_id": order_id, "pizza_type": pizza_type, "customer_name": customer_name, "customer_address": customer_address, "customer_email": customer_email, "customer_phone": customer_phone}
    
    # Send message to Kafka topic
    producer.send("pizza-orders", key=message_key, value=message_value)
    
    # Flush to ensure message is sent immediately
    producer.flush()
    
    # Calculate time elapsed and print message
    current_time = time.time()
    time_elapsed = current_time - last_send_time
    print(f"Message sent to Kafka. Time elapsed: {time_elapsed:.2f} seconds. ⭐⭐⭐⭐⭐")
    
    # Update last_send_time for next iteration
    last_send_time = current_time
    
    # Sleep for a random interval between 1 to 2 second
    time.sleep(random.uniform(1, 2))