from django.shortcuts import render
from django.http import HttpResponse
import os
from .forms import eventForm
from myproject.settings import BASE_DIR

p = os.path.join(BASE_DIR,"templates")
# Create your views here.

def home(request):
    return render(request, 'speakers/home.html', {'home':home})
def event_list(request):
    events = get_object_or_404(event, pk=event_id)
    return HttpResponse(render(request, 'speakers/event_list.html', {'event': event}))
def s(request):
    return HttpResponse(request, 'welcome')
def event(request):
    return HttpResponse(render(request, 'speakers/event.html', {}))

     