from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'content': 'Friendship Home Page'
    }
    return render(request, 'friendships/friendship_home.html', context)

def request(request):
    context = {
        'content': 'Friendship Request Page'
    }
    return render(request, 'friendships/friendship_request.html', context)