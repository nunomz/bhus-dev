import json 
from kafka import KafkaConsumer

#outfile = open('speedometer.json', 'ab')
#nl = "\n"
nl = b"\n"
if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'test',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest'
    )
    for message in consumer:
        print(json.loads(message.value))
        with open('sensorcluster_output.json', 'ab') as outfile:
            outfile.write(message.value+nl)