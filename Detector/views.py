from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os




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