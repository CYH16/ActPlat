from .models import Post, Like
from django.utils import timezone
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

# Create your views here.
def activity_list(request):
    posts = Post.objects.filter(結束日期與時間__gte=timezone.now()).order_by('開始日期與時間')
    if request.method == "POST":
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')
        else:
            return render(request, 'activity_platform/activity_list.html',locals())
    
    else:
        return render(request, 'activity_platform/activity_list.html',locals())
		
def activity_mine(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    else:
        user = request.user.username
        posts = Like.objects.get(user=user).post.all()
        return render(request, 'activity_platform/activity_mine.html',locals())		

def activity_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')
        else:
            
            #post = Post.objects.get(id=request.POST['id'])
            user = request.user.username
            
            if not Like.objects.filter(user=user):
                Like.objects.create(user=user).post.add(post)
            else:
                #return HttpResponse(Like.objects.get(user=user).restaurant.all())
                
                if post not in Like.objects.get(user=user).post.all():
                    Like.objects.get(user=user).post.add(post)
                else:
                    Like.objects.get(user=user).post.remove(post)
            allpost = Like.objects.get(user=user).post.all()
            return render(request, 'activity_platform/activity_detail.html',locals())
    else:
        if not request.user.is_authenticated():
            return render(request, 'activity_platform/activity_detail.html', {'post': post})
        else:
            user = request.user.username
            if not Like.objects.filter(user=user):
                return render(request, 'activity_platform/activity_detail.html', locals())
            else:
                allpost = Like.objects.get(user=user).post.all()
                return render(request, 'activity_platform/activity_detail.html', locals())
    
	
def activity_about(request):
    return render(request, 'activity_platform/activity_about.html', {})
	
def login(request):
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/')

    error = False
    
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
    
        user = auth.authenticate(username=username, password=password)
    
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = True
            return render(request, 'activity_platform/login.html', locals())
    else:
        return render(request, 'activity_platform/login.html', locals())
		
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'activity_platform/register.html',locals())