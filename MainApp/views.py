from django.shortcuts import render, redirect

from .forms import TopicForm
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()

    context = {'topics': topics} # The key is what is used in the HTML file; the value is what is used in views.py (easiest to use the same name; QED)

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id): # Second argument has to be consistent with what was defined in urls.py
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.all().order_by('-date_added') # '-' is the same as order by <attr> desc in SQL

    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST': # Check to see if the request is a 'GET' request (new blank form) or a 'POST' request (submission of filled-out form)
        form = TopicForm()
    else: # (i.e., a 'GET' request)
        form = TopicForm(data = request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect('MainApp:topics')
    
    context = {'form':form}

    return render(request, 'MainApp/new_topic.html', context)

