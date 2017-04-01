from django.conf.urls import url
from .views import home, send_message, get_convn

urlpatterns = [
   url(r'^$', home, name="home"),
   url(r'^sendmessage/',send_message, name="send message"),
   url(r'^getconv/(?P<sender_id>[0-9])/(?P<receiver_id>[0-9])/', get_convn, name="get conversation"),
]
