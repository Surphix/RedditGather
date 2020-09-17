import os, sys
from uuid import uuid4
from confluent_kafka import Producer

class produce_k:

    def __init__(self, count, server):
        print("Boostrap server: {server}".format(server=server))

        conf = {'bootstrap.servers': server}
        self.p = Producer(conf)
        self.flush_limit = count
        self.count = 0

    @staticmethod
    def delivery_callback(err, msg):
        if err:
            sys.stderr.write('%% Message failed delivery: %s\n' % err)
        else:
            sys.stderr.write('%% Message successfully delivered to %s [%d] @ %d\n' % 
                            (msg.topic(), msg.partition(), msg.offset()))

    def send(self, topic, obj):
        try:
            if self.count >= self.flush_limit:
                self.flush()

            self.p.produce(topic=topic, key=str(uuid4()), value=obj, on_delivery=self.delivery_callback)
            self.count += 1     
        except BufferError:
            sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                            len(self.p))

    def flush(self):
        self.p.poll(0)
        self.p.flush()
        self.count = 0