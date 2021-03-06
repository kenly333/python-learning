import pika

#credentials = pika.PlainCredentials('admin', 'public')
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_test_exchange')


result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = ['error', ]

for severity in severities:
    channel.queue_bind(exchange='direct_test_exchange',
                       queue=queue_name,
                       routing_key=severity)
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()