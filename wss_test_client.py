from websocket import create_connection
import datetime

def subscribe(url):
    try:
        ws = create_connection(url,timeout=250)
        if ws.connected:
            while 1:
                data = ws.recv()
                print(datetime.datetime.now(), data)
            ws.close()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    subscribe("ws://127.0.0.1:8000/notify/")
