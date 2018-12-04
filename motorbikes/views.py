from django.shortcuts import render
from django.utils import timezone
from .models import Post_MB

def motorbikes(request):
    posts_MB = Post_MB.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'motorbikes/motorbikes.html', {'posts_MB': posts_MB})