from django.shortcuts import render
from time import localtime, strftime  # Changed from gmtime to localtime for local timezone
# Create your views here.

def index(request):
    context = {
        "time": strftime("%B %dth %Y", localtime()),
        "date":strftime("%I:%M %p",localtime())
    }
    return render(request, 'index.html', context)

