import json 
from kafka import KafkaConsumer

def start():
    #nl = b"\n"
    # Kafka Consumer - CloudKarafka
    topic='ussvswrg-sensores'
    consumer = KafkaConsumer(
        topic,\
        security_protocol='SASL_SSL',\
        sasl_mechanism='SCRAM-SHA-256',\
        sasl_plain_username='ussvswrg',\
        sasl_plain_password='k_1BTu_ujWmgCOU5WSd4AK0dGJPxrINB',\
        bootstrap_servers='glider.srvs.cloudkafka.com:9094',\
        #group_id='bhus-server',\
        auto_offset_reset='latest'
    )
    #print(consumer.config['api_version'])
    for message in consumer:
        mensagem = json.loads(message.value)
        print('\tCONSUMED: '+str(mensagem))
        # if mensagem.get("bus_id") == '081':
        #     with open('bd/081/sensorcluster_output.json', 'ab') as outfile:
        #         outfile.write(message.value + b"\n")
        # elif mensagem.get("bus_id") == '103':
        #     with open('bd/103/sensorcluster_output.json', 'ab') as outfile:
        #         outfile.write(message.value + b"\n")
        with open('bd/' + str(mensagem.get("bus_id")) + '/sensorcluster_output.json', 'ab') as outfile:
                 outfile.write(message.value + b"\n")