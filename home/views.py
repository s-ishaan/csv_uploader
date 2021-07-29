from django.shortcuts import render
import pandas as pd
from kakcho_task import ops



# def upload_to(instance,filename):
#     return 'posts/{filename}'.format(filename=filename)

# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'upload.html')
    else:
        return render(request, 'index.html')



def download(request):
    return render(request, 'download.html')


def upload(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['doc']
        csv = pd.read_csv(uploaded_file, sep=',')
        ops.rate_diff(csv)
        # path = os.path.join(settings.BASE_DIR, 'paid_apps.csv')
        # print(path)

        # return render(request, 'upload.html', storage)

    return render(request, 'upload.html')


# def download_file(request):
#     # fill these variables with real values
#     fl_path = 'media\hello.txt'
#     filename = 'hello.txt'
#     fl = open(fl_path)
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response



