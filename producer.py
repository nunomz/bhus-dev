import random 
import string 

user_ids = list(range(1, 101))
velocity_range = list(range(30, 55))
temperature_range = list(range(15, 25))

import wmi
w_temp=wmi.WMI(namespace="root\\wmi")
print((w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15)

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
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = generate_message()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('test', dummy_message)
        producer.flush()
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)