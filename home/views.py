from django.shortcuts import render, redirect
import pandas as pd
from kakcho_task import ops
import os
from kakcho_task import settings


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

    

