from django.shortcuts import render
from django.http import HttpResponse

from app.models import Users


def index(request):
    return render(request, 'login.html')

def authenticate(request):
    authenticate = Users.authenticate(request.POST.get('email'), request.POST.get('password'))
    if not authenticate:
        return HttpResponse("Wrong credentials. Try again.")
    
    return page(request, 'home.html', request.POST.get('email'))

def page(request, page, email):
    user = Users.objects.get(email=email)
    return render(request, page, {'user': user, 'mails_sent': user.mails_sent(), 'mails_received': user.mails_received(), 'mails_spam': user.mails_spam()})