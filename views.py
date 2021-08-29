from django.shortcuts import render
from website.models import Video
# Create your views here.

def homepage(request):
    video = Video.objects.all()
    
    return render(request,'homepage.html',{"video":video})