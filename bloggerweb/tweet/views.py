from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm ,UserRegistrationForm #he database that match certain criteria, or return a 404 Not Found response if no objects match the criteria.
from django.contrib.auth.decorators import login_required # for protect tweet creation from all user 
from django.contrib.auth import login


from django.db.models import Q #search ing for
# Create your views here.

def index (request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


#search for tweet in tweet list 
def tweet_list(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        # Filter tweets that contain  in the text or username
        tweets = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        ).order_by('-created_at')
    else:
        # If no query, show all tweets
        tweets = Tweet.objects.all().order_by('-created_at')
    
    return render(request, 'tweet_list.html', {'tweets': tweets})


''''
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  #the - prefix denotes descending
    return render(request,'tweet_list.html', {'tweets': tweets}) #we retuen this page all tweet
'''

#crud operations
#for tweet creat 
@login_required

def tweet_create(request):  # Handle tweet creation requests
    if request.method == "POST":  # Check if the request is a form submission
        form = TweetForm(request.POST, request.FILES)  # combind form with submitted data and files
        if form.is_valid():  # Validate the form data
            tweet = form.save(commit=False)  # Create tweet object but don’t save yet
            tweet.user = request.user  # Assign the logged-in user as the tweet author
            tweet.save()  # Save the tweet to the database
            return redirect('tweet_list')  # Redirect to the tweet list page
    else:  # If not a POST request
        form = TweetForm()  # Initialize an empty form
    return render(request, 'tweet_create.html', {'form': form})  # Render the form page

#for tweet edit 
@login_required

def tweet_edit(request, tweet_id):
    # Fetch the tweet instance for the logged-in user
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        # Combine submitted data and files with the tweet instance
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()  # Save the updated tweet
            return redirect('tweet_list')  # Redirect to the tweet list page
    else:
        # Pre-fill the form with the tweet instance
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_create.html', {'form': form})


 #for tweet delete 
'''
def tweet_delete(request, tweet_id):  # Handle tweet deletion
    tweet = get_list_or_404(Tweet, pk=tweet_id, user=request.user)  # Get the tweet if it exists and belongs to the user
    if request.method == "POST":  # Check if the request is a form submission
        tweet.delete()  # Delete the tweet from the database
        return redirect('tweet_list')  # Redirect to the tweet list page
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})  # Render a confirmation page for deletion

 '''
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Fetch only the user's tweet
    if request.method == "POST":
        tweet.delete()  # Delete the tweet
        return redirect('tweet_list')  # Redirect to tweet list
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})  # Confirm page for GET
   



# register view

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)  # Create form instance with POST data
        if form.is_valid():  # Check if the form is valid
            user = form.save(commit=False)  # Create user object but don't save it yet
            user.set_password(form.cleaned_data['password1'])  # Set the password after hashing
            user.save()  # Save the user instance
            login(request, user)  # Log the user in
            return redirect('tweet_list')  # Redirect to the tweet list after successful registration
    else:
        form = UserRegistrationForm()  # Initialize the form for GET request

    # Render the registration page with the form
    return render(request, 'registration/register.html', {'form': form})



    