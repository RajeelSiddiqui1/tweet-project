from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import User, UserTweets
from .forms import TweetsForm, UserRegisterationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


#admin signup


def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = UserTweets.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html',{'tweets':tweets})

#create
@login_required
def tweet_create(request):
    if request.method == "POST":
       form = TweetsForm(request.POST, request.FILES)
       if form.is_valid():
           tweet = form.save(commit=False)
           tweet.name = request.user
           tweet.save()
           return redirect('tweet_list')

    else:
       form = TweetsForm()
    return render(request,'tweet_form.html',{'form':form})

#edit
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(UserTweets, pk=tweet_id, name=request.user)
    if request.method == "POST":
        form = TweetsForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.name = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetsForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

#delete
@login_required
def tweet_delete (request, tweet_id):
    tweet = get_object_or_404(UserTweets, pk=tweet_id, name = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

#register
def register (request):
    
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
          user = form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
          login(request, user)
          return redirect('tweet_list')
        
    else:
     form = UserRegisterationForm()

    return render(request,'registration/register.html',{'form':form})
