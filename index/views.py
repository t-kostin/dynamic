from django.shortcuts import render
from django.utils import timezone

def index(request, *args, **kwargs):

    current_utc= timezone.now()
    local_time = timezone.localtime(current_utc)
    context = {
        'local_time': local_time.strftime('%H:%M'),
    }

    return render(request, 'index.html', context)
