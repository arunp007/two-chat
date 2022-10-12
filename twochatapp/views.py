from django.shortcuts import render
from django.http import HttpResponse
from.models import *

def home(request):
    return render(request, 'home.html')

def chat1(request):
    if request.method == 'POST':
        text1 = request.POST['text1']
        user_details = Chat1(text1=text1)
        user_details.save()
    user_data1 = Chat1.objects.all()
    user_data2 = Chat2.objects.all()
    return render(request, 'chat1.html', {'user1': user_data1 , 'user2': user_data2})

def chat2(request):
    if request.method == 'POST':
        text2 = request.POST['text2']
        user_details = Chat2(text2=text2)
        user_details.save()
    user_data1 = Chat1.objects.all()
    user_data2 = Chat2.objects.all()
    return render(request, 'chat2.html', {'u1': user_data1, 'u2' : user_data2})
