# public_build/consumers.py
from abc import ABCMeta,abstractmethod
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class AbsWebsocketConsumer(WebsocketConsumer, metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        WebsocketConsumer.__init__(self, *args, **kwargs)

        self.__host = None
        self.__port = None
        if len(args) > 0:
            k = args[0]
            if "client" in k.keys():
                if len(k["client"]) > 1:
                    self.__host = k["client"][0]
                    self.__port = k["client"][1]

        self.__group_name = self.get_group_name()

    @abstractmethod
    def set_group_name(self):
        """获取组名,子类重写
            返回：组名称
        """
        pass

    def get_conn(self):
        return self.__host, self.__port

    def connect(self):

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.__group_name,
            self.channel_name
        )

        self.accept()
        self.on_connect()

    def on_connect(self):
        pass

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.__group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        pass

    # Send message to group
    def send_channel_layer(msg, group_name):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send_message",
                'message':msg
            }
        )

    # Receive message from room group
    def send_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=message)
