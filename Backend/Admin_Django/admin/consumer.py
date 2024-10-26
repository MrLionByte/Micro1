import pika

params = pika.URLParameters("amqps://tmzwuyef:v8gqvHcDLrJS5RKNzkKvjKSeDlNslbEn@crow.rmq.cloudamqp.com/tmzwuyef")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recivied in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('Started Consumeing')

channel.start_consuming()

channel.close()