#!/usr/bin/env python

import websocket
import thread
import time
import json

def on_message(ws, message):
    print message + "caca"

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())


websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://echo.websocket.org/",
						  on_message = on_message,
						  on_error = on_error,
						  on_close = on_close)
ws.on_open = on_open
ws.run_forever()

