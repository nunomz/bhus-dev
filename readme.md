# Usage:
- install kafka: https://kafka.apache.org/downloads
- cd to kafka folder
- bin/zookeeper-server-start.sh config/zookeeper.properties
- (in another terminal) bin/kafka-server-start.sh config/server.properties
- in this folder:
    - run producer
    - run consumer
    - run serv
    - sudo socketxp connect http://localhost:5000
    
## to create topic:
- $ bin/kafka-topics.sh --create --topic [name] --bootstrap-server localhost:9092

## a fazer
- diferentes ids de autocarro na app.
- ao fazer o get meter o id do autocarro como parametro
- flask procura no ficheiro pelo id do autocareo

## erro:
- rm -rf logs
# References:
- https://kafka.apache.org/quickstart
- https://betterdatascience.com/apache-kafka-in-python-how-to-stream-data-with-producers-and-consumers/
- https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05