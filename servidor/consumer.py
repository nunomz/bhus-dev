import json 
from kafka import KafkaConsumer

nl = b"\n"

if __name__ == '__main__':
    # Kafka Consumer - CloudKarafka
    topic='ussvswrg-sensores'
    consumer = KafkaConsumer(
        topic,\
        security_protocol='SASL_SSL',\
        sasl_mechanism='SCRAM-SHA-256',\
        sasl_plain_username='ussvswrg',\
        sasl_plain_password='k_1BTu_ujWmgCOU5WSd4AK0dGJPxrINB',\
        bootstrap_servers='glider.srvs.cloudkafka.com:9094',\
        auto_offset_reset='latest'
    )
    
    for message in consumer:
        print(json.loads(message.value))
        with open('sensorcluster_output.json', 'ab') as outfile:
            outfile.write(message.value+nl)