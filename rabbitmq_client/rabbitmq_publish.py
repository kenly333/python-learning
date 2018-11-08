import pika

#credentials = pika.PlainCredentials('admin', 'public')

#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                  routing_key='hello',
                  body='Hello World!')
print("开始队列")

connection.close()