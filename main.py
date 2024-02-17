import json
from kafka import KafkaProducer

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

producer.send("pizza-orders", key={"order_id": 1}, value={"order_id": 1, "pizza_type": "pepperoni"})

producer.flush()