from django.shortcuts import render
from django.http import JsonResponse
from .models import Message, User
from django.utils.timezone import localtime
import json

def home(request):
    """
    Returns all users which are sorted in order of latest message being recieved.
    """
    users = User.objects.all()
    context = []
    for user in users:
        response = {}
        message = Message.objects.filter(sender=user.id)
        if not message:
            response['last_message'] = {'text': 'No last messages', 'sender_id' : 0, 'time' : 0}
        else:
            for i in message:
                msg = i
            response['last_message'] = {'text': msg.text, 'receiver_id' : msg.receiver.id, 'time' : msg.time.isoformat()}
        response['name'] = user.username
        response['user_id'] = user.id
        context.append(response)
    context.sort(key=lambda item:item['last_message']['time'], reverse=True)
    return JsonResponse(context, safe=False)

def send_message(request):
    if request.method == 'POST':
        msg = request.POST.get('message',"")
        sender_id = request.POST.get('sender_id','')
        receiver_id = request.POST.get('receiver_id', '')
        response = {}
        if sender_id and receiver_id:
            sender_obj = User.objects.filter(id=sender_id)
            receiver_obj = User.objects.filter(id=receiver_id)
            message = Message(text=msg, sender=sender_obj[0], receiver=receiver_obj[0])
            message.save()
            response['msg'] = "Message sent successfully"
            response['status'] = "success"
        else:
            response['msg'] = "Message sending failed"
            response['status'] = "fail"
        return JsonResponse(response)
    elif request.method == 'GET':
        return home(request)


def get_convn(request, sender_id="", receiver_id=""):
    sender = User.objects.filter(id=sender_id)
    receiver = User.objects.filter(id=receiver_id)
    if sender.count() == 0:
        return JsonResponse({'msg': 'No user with id %s'%sender_id}, safe=False)
    elif receiver.count() == 0:
        return JsonResponse({'msg': 'No user with id %s'%receiver_id}, safe=False)
    message1 = Message.objects.filter(sender=sender)
    message2 = Message.objects.filter(sender=receiver)
    message = []
    for m,n  in message1, message2:
        message.append(m)
        message.append(n)
    context = []
    for m in message:
        response = {}
        response['text'] = m.text
        response['sender'] = m.sender.username
        response['receiver'] = m.receiver.username
        response['time'] = m.time.isoformat()
        context.append(response)
    context.sort(key=lambda item:item['time'], reverse=True)
    return JsonResponse(context, safe=False)
