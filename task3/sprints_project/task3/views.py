from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .models import Courses
from .forms import PostForm
from django.views.generic.edit import CreateView
# Create your views here.

def Welcome(request):
 # return HttpResponse("Welcome to our site")
    template = loader.get_template('cv.html')
    return HttpResponse(template.render())

class StudentCreate(CreateView):
      # specify the model for create view
      model = Student
      # specify the fields to be displayed
      fields = ['name', 'phone', 'address']

def home_view(request):
    if request.method == 'POST':
        details = PostForm(request.POST)
        if details.is_valid():
            return HttpResponse("Data Submitted Successfully")
        else:
            return render(request, 'home.html', {'form': details})
    else:
        form = PostForm(None)
        return render(request, 'home.html', {'form': form})
