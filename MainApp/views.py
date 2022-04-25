from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()

    context = {'topics': topics} # The key is what is used in the HTML file; the value is what is used in views.py (easiest to use the same name; QED)

    return render(request, 'MainApp/topics.html', context)
