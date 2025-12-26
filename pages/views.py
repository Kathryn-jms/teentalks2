from django.shortcuts import render, get_object_or_404
from .models import Topic

def home(request):
    return render(request, 'pages/home.html')

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'pages/topic_list.html', {'topics': topics})



def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    related_topics = Topic.objects.exclude(id=topic_id)[:3]

    return render(request, 'pages/topic_detail.html', {
        'topic': topic,
        'related_topics': related_topics
    })











