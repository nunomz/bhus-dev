import random 
import string 

user_ids = list(range(1, 101))
velocity_range = list(range(30, 55))
temperature_range = list(range(15, 25))

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    # Copy the recipients array
    recipient_ids_copy = velocity_range.copy()
    # User can't send message to himself
#    recipient_ids_copy.remove(random_user_id)
    velocity_message = random.choice(velocity_range)
    temperature_message = random.choice(temperature_range)
    return {
        'bus_id': random_user_id,
        'velocity': velocity_message,
        'temperature': temperature_message
    }

## separar

import time 
import json 
import random 
from datetime import datetime
#from data_generator import generate_message
from kafka import KafkaProducer

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
    #bootstrap_servers='pg50670-vpf3gbo46iewetr9.socketxp.com',
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = generate_message()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('ussvswrg-sensores', dummy_message)
        producer.flush()
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)