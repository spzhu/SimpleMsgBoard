from django.shortcuts import render
from .models import UserMessage


# Create your views here.
def getform(request):
    all_message = UserMessage.objects.filter(name="zsp")
    if all_message:
        message = all_message[0]

    return render(request, "messageform.html", {"mymessage": message})
