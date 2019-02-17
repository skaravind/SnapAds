from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from wsgiref.util import FileWrapper
from django.core.files import File
from django.http import HttpResponse
import mimetypes


def cleanup():
    files = [f for f in os.listdir('media/')]
    for f in files:
        os.remove('media/'+f)


def index(request):
    if request.method == 'POST':

        myfile = request.FILES['objFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        fname = myfile.name
        uploaded_file_url = fs.url(filename)

        return render(request, 'frontend/index.html', {
            'uploaded_file_url': uploaded_file_url,
        })
    return render(request, 'frontend/index.html')


def download(request,file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(File(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name) 
    return response