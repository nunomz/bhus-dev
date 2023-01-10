import random
import string
import sensorSingleton 

import time 
import json 
import random 
from datetime import datetime
from kafka import KafkaProducer

singleton_instance = sensorSingleton.Singleton.get_instance()

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['glider.srvs.cloudkafka.com:9094'],\
    security_protocol='SASL_SSL',\
    sasl_mechanism='SCRAM-SHA-256',\
    sasl_plain_username='ussvswrg',\
    sasl_plain_password='k_1BTu_ujWmgCOU5WSd4AK0dGJPxrINB',\
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        message = singleton_instance.generate_message()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(message)}')
        producer.send('ussvswrg-sensores', message)
        producer.flush()
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)