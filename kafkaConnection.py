from kafka import KafkaProducer
import json

def publish_message(producer_instance, topic_name, data):
    """
    This function accepts producer instance, topic name and data as input.
    It is dynamic method,
    which can be used to publish data to any topic provided
    """
    try:
        producer_instance.send(topic_name, data)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    """
    This function will create instance of kafka producer 
    """
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer
