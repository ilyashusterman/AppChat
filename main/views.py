from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User
from .models import Messages

def home(request):
    messages = Messages.objects.all()
    users = User.objects.all()
    return render(request, 'index.html', {'users': users, 'messages': messages})

