from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def index(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects_to_show = [
        {
            'title': 'Greeting_app',
            'path': 'images/Greet_app.PNG',
        },

        {
            'title': 'CRUD',
            'path': 'images/CRUD.PNG',
        },

         {
            'title': 'Photo Uploader',
            'path': 'images/Photo Uploader.PNG',
        },

        {
            'title': 'Portfolio',
            'path': 'images/portfolio.PNG',
        },
        {
            'title': 'Tweet_app',
            'path': 'images/Tweet_app.PNG',
        },]
    return render(request, 'project.html',{"projects_to_show": projects_to_show})

def certificate(request):
    return render (request, "certificate.html")

def contact(request):
    return render (request,"contact.html")


def resume(request):
    resume_path="myapp/MahammedAli.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="MahammedAli.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)