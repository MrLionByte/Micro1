import pika
import json

params = pika.URLParameters("amqps://tmzwuyef:v8gqvHcDLrJS5RKNzkKvjKSeDlNslbEn@crow.rmq.cloudamqp.com/tmzwuyef")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='main', body=json.dumps(body), properties=properties)