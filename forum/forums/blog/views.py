from django.shortcuts import render, redirect
from datetime import datetime
from .models import Thought
from .forms import Searchform
from .chatgpt import random_thought
import json 
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Thought

def random(request):
    context = random_thought()
    thought = Thought(topic = context['title'],desc=context['thought'])
    thought.date = datetime.today()
    thought.save()
    return render(request,'index.html')

@csrf_exempt
def like_thought(request):
    data = json.loads(request.body.decode('utf-8'))
    thought_id = data.get('thoughtId')
    thought = Thought.objects.get(pk=thought_id)
    thought.likes += 1  # Increment likes
    thought.save()
    return JsonResponse({'likes': thought.likes, 'dislikes': thought.dislikes})
    
@csrf_exempt
def dislike_thought(request):
    data = json.loads(request.body.decode('utf-8'))
    thought_id = data.get('thoughtId')
    thought = Thought.objects.get(pk=thought_id)
    thought.dislikes+=1
    thought.likes-=1
    thought.save()
    return JsonResponse({'dislikes':thought.dislikes,'likes':thought.likes})

def index(request):
    form = Searchform()
    thoughts = Thought.objects.all()
    
    if 'query' in request.GET:
        form = Searchform(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            thoughts = Thought.objects.filter(topic__icontains=query) | Thought.objects.filter(desc__icontains=query)

    context = {
        'thoughts': thoughts,
        'form':form
    }
    return render(request, 'index.html', context)

def delete_thought(request):
    if request.method == 'POST':
        for id in request.POST.getlist('deleted-thoughts'):
            Thought.objects.filter(thought_id=id).delete()
    return render(request,'index.html')

def create_thought(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        desc = request.POST.get('desc')
        date = datetime.today().date()

        # Ensure values are not None or empty
        if topic and desc:
            thought = Thought(topic=topic, desc=desc, date=date)
            thought.save()
            return render(request,'index.html')
        else:
            # Handle the case where required fields are missing
            return render(request, 'index.html', {'error': 'All fields are required.'})

    return render(request, 'add_thought.html')
