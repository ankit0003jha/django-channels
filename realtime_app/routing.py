from django.urls import path

from .consumers import WSConsumer , NewConsumer

ws_urlpatterns = [

    path('ws/some_url/' , WSConsumer.as_asgi()),
    #path('ws/send/' , NewConsumer.as_asgi()),


]