from kafka import KafkaConsumer
import json
from dataToPass import get_country_data
from kafkaConnection import connect_kafka_producer, publish_message
import requests


if __name__ == '__main__':
    """
    Only one topic is getting crated for country!
    This part will get data for country
    connect with kafka producer and publich the message.
    Other part of this function will create kafka consumer
    and listen for topic and retrieve message.
    Retrieved messages will be passed to REST API.
    """
    print "**** Producer Part ****"
    country_data = get_country_data()
    topic_name = 'country_data'
    if country_data:
        kafka_producer = connect_kafka_producer()
        publish_message(kafka_producer, topic_name, country_data)
        if kafka_producer is not None:
            kafka_producer.close()

    print "**** Consumer Part ****"
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    consumer.subscribe([topic_name])
    print "Message Received successfully"

    # URL for external api call, to post the data in DB
    url = 'http://127.0.0.1:8000'
    end_point = '{}/country/'.format(url)
    for msg in consumer:
        try:
            r = requests.post(end_point, msg.value)
            if r.status_code == 200:
                print r.text
            else:
                print "Error Raised"
                print r.text
        except Exception as ex:
            print('Exception in calling external API')
            print(str(ex))
    consumer.close()