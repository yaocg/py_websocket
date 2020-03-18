

# py_websocket
## 订阅-通知



## 运行

1. 运行通知服务
```
# 命令
python3 manage.py runserver 0.0.0.0:8000

# 结果
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

March 18, 2020 - 10:58:51
Django version 3.0.2, using settings 'py_websocket.settings'
Starting ASGI/Channels version 2.4.0 development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
start notify...
WebSocket HANDSHAKING /notify/ [127.0.0.1:49903]
WebSocket CONNECT /notify/ [127.0.0.1:49903]
2020-03-18 10:58:57.045104 no:1 routine notify for py_websocket!!!
2020-03-18 10:59:02.047198 no:2 routine notify for py_websocket!!!
2020-03-18 10:59:07.050108 no:3 routine notify for py_websocket!!!
2020-03-18 10:59:12.046982 no:4 routine notify for py_websocket!!!
WebSocket HANDSHAKING /notify/ [127.0.0.1:49912]
WebSocket CONNECT /notify/ [127.0.0.1:49912]
```


2. 运行订阅客户端
```
# 命令
python3 wss_test_client.py

# 结果
2020-03-18 18:58:53.637631 hello py_websocket!!!
2020-03-18 18:58:57.054566 no:1 routine notify for py_websocket!!!
2020-03-18 18:59:02.058627 no:2 routine notify for py_websocket!!!
2020-03-18 18:59:07.057130 no:3 routine notify for py_websocket!!!
2020-03-18 18:59:12.053171 no:4 routine notify for py_websocket!!!
2020-03-18 18:59:17.051579 no:5 routine notify for py_websocket!!!
2020-03-18 18:59:22.057800 no:6 routine notify for py_websocket!!!
2020-03-18 18:59:27.060342 no:7 routine notify for py_websocket!!!
```
