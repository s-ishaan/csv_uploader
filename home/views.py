from django.shortcuts import render, redirect
import pandas as pd
from kakcho_task import ops
import os
from kakcho_task import settings
from django.http import HttpResponse


# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/upload')
    else:
        return render(request, 'index.html')


def download(request):
    context={}
    app_list = ['paid_apps','free_apps','everyone_apps','everyone_ten','teen_apps','mature_apps','adults_apps','unrated_apps']
    for app in app_list:
        context[app] = f'file:///{os.path.join(settings.BASE_DIR, f"{app}.csv")}'
    
    return render(request, 'download.html', context)


def upload(request):   
    if request.method == 'POST':
        uploaded_file = request.FILES['doc']
        csv = pd.read_csv(uploaded_file)
        ops.rate_diff(csv)
        ops.content_rating_diff(csv)
        ops.rating_round_off(csv)

    return render(request, 'upload.html')

def get_paid(request):  
    with open('paid_apps.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=paid_apps.csv'
        return response
  
def get_free(request):  
    with open('free_apps.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=free_apps.csv'
        return response
  
def get_ev(request):  
    with open('everyone_apps.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=everyone_apps.csv'
        return response
  
def get_ev_ten(request):  
    with open('everyone_ten.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=everyone_ten_apps.csv'
        return response

def get_teen(request):  
    with open('teen_apps.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=teen_apps.csv'
        return response

def get_mature(request):  
    with open('mature_apps.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=mature_apps.csv'
        return response

def get_adult(request):  
    with open('adults_apps.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=adult_apps.csv'
        return response

def get_unrated(request):  
    with open('unrated_apps.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=unrated_apps.csv'
        return response

def get_round(request):  
    with open('round_off.csv', encoding='utf8') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=round_off.csv'
        return response



