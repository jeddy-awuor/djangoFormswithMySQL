from django.shortcuts import render
from django.http import HttpResponse
from djangoForms.forms import Wanafunzi
from djangoForms.functions import handle_uploaded_files

def index(request):
    if request.method == 'POST':
        stud = Wanafunzi(request.POST, request.FILES)
        if stud.is_valid():
            handle_uploaded_files(request.FILES['file_uploaded'])
            return HttpResponse ("Uploaded file successfully")
    else:
        stud = Wanafunzi()
        return render(request, 'index.html',{'form': stud})
