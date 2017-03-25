from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def activity_list(request):
    #posts = Post.objects.all().order_by('開始日期與時間')
    posts = Post.objects.filter(結束日期與時間__gte=timezone.now()).order_by('開始日期與時間')
    return render(request, 'activity_platform/activity_list.html', {'posts': posts})
	
def activity_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'activity_platform/activity_detail.html', {'post': post})