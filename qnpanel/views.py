from django.shortcuts import render
from .models import quiz

# Create your views here.
def home(request):
    qn=quiz.objects.all()
    n=len(qn)
    return render(request,'home.html',{'qn':qn,'numquiz': n})
