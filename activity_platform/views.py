from .models import Post, Like
from .forms import Add_new
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

def add_new(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    else:
        if request.method == 'POST':
            errors = False
            f = Add_new(request.POST, request.FILES)
            if f.is_valid():
                活動名稱 = f.cleaned_data['活動名稱']
                副標題 = f.cleaned_data['活動副標題']
                圖片 = f.cleaned_data['圖片']
                簡介 = f.cleaned_data['簡介']
                開始日期與時間 = f.cleaned_data['開始日期與時間']
                結束日期與時間 = f.cleaned_data['結束日期與時間']
                地點 = f.cleaned_data['簡單地點']
                對象 = f.cleaned_data['活動對象']
                費用 = f.cleaned_data['簡單費用']
                人數限制 = f.cleaned_data['人數限制']
                報名死線 = f.cleaned_data['報名截止日期與時間']
                聯絡資訊 = f.cleaned_data['聯絡資訊']
                類型 = f.cleaned_data['類型']
                標籤 = f.cleaned_data['性質']+" "+f.cleaned_data['類型']+" "+f.cleaned_data['費用分類']+" "+f.cleaned_data['活動對象分類']
                詳細地點 = f.cleaned_data['詳細地點']
                詳細費用 = f.cleaned_data['詳細費用']
 
                Post.objects.create(活動名稱=活動名稱, 副標題=副標題, 圖片=圖片, 簡介=簡介, 開始日期與時間=開始日期與時間, 結束日期與時間=結束日期與時間, 地點=地點, 對象=對象, 費用=費用, 人數限制=人數限制, 報名死線=報名死線, 聯絡資訊=聯絡資訊, 類型=類型, 標籤=標籤, 詳細地點=詳細地點, 詳細費用=詳細費用)
			
                return HttpResponseRedirect('/')
            else:
                errors = True
                return render(request, 'activity_platform/add_new.html',locals())
        else:
            return render(request, 'activity_platform/add_new.html',locals())