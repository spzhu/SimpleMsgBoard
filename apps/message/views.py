from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def getform(request):
    user_messages = UserMessage()
    user_messages.name = "zsp"
    user_messages.address = "北京"
    user_messages.email = "213@123.com"
    user_messages.message = "helloworld"
    user_messages.object_id = "helloworld"
    user_messages.save()

    return render(request, "messageform.html")
