# notify/consumers.py
from public_build.websocket_consumer import AbsWebsocketConsumer

class Consumer(AbsWebsocketConsumer):
    __group_name = "py_websocket_notify"

    def set_group_name(self):
        Consumer.get_group_name()

    @staticmethod
    def get_group_name():
        return Consumer.__group_name

    def on_connect(self):
        self.send(text_data="hello py_websocket!!!")

