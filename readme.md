# Usage:
- server:
    - run consumer
    - run server
    - sudo socketxp connect http://localhost:5000
- autocarro:
    - run producer
    - change url variable on post_qr function (ticket_validator.py)
    - run ticket validator


## to create topic:
- $ bin/kafka-topics.sh --create --topic [name] --bootstrap-server localhost:9092

## melhoramentos
- diferentes ids de autocarro na app.
- ao fazer o get meter o id do autocarro como parametro
- flask procura no ficheiro pelo id do autocareo

## erro:
- rm -rf logs

# References:
- https://kafka.apache.org/quickstart
- https://betterdatascience.com/apache-kafka-in-python-how-to-stream-data-with-producers-and-consumers/
- https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05