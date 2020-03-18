from apscheduler.schedulers.background import BackgroundScheduler

from .consumers import Consumer
import datetime

no = 0
def notify():
    global no
    no += 1
    message = "no:{} routine notify for py_websocket!!!".format(no)
    print(datetime.datetime.now(), message)
    Consumer.send_channel_layer(message, Consumer.get_group_name())

scheduler = BackgroundScheduler()
scheduler.add_job(notify, 'interval', seconds=5)
scheduler.start()

print("start notify...")
