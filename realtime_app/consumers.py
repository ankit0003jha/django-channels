import json
from random import randint
from time import sleep


from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()


        for i in range(1,10):
            self.send(json.dumps({ 'message' : i}))
            sleep(1)


class NewConsumer(SyncConsumer):
    def websocket_connect(self , event):
        print('connect event is called')
        self.send(
            {'type' : 'websocket.accept'
        })

        
        
    def websocket_receive(self , event): 
        print(event) 
        self.send(
            {'type' : 'websocket.send',
            'text' : event.get('text')
        }) 
    


    def websocket_disconnect(self , event): 
        print('connection is disconnected')  
        print(event)