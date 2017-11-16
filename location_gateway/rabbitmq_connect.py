import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
class MessageQueue:

    def __init__(self):
        self.url = os.environ.get('CLOUDAMQP_URL', 'amqp://user:pa@localhost:5672/%2f')
        self.params = pika.URLParameters(self.url)
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue='hello') # Declare a queue




    def send_addr_data():
        self.channel.basic_publish(exchange='',
                            routing_key='hello',
                            body='Hello CloudAMQP!')


    def __del___(self):
        self.connection.close()



x = MessageQueue()

