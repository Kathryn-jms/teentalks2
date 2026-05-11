
from django.shortcuts import render, get_object_or_404
from .models import Tip


def tips_list(request):
    tips = Tip.objects.all()
    return render(request, 'tips/tips_list.html', {'tips': tips})


def tip_detail(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    return render(request, 'tips/tip_detail.html', {'tip': tip})

def tips_home(request):
    return render(request, 'tips/tips.html')
