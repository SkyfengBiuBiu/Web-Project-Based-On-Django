from django.shortcuts import render

# Create your views here.
def home(request,user_id):
    context = {
        'content': 'Friendship Home Page'
    }
    return render(request, 'friendships/friendship_home.html', context)

def request(request,user_id):
    context = {
        'content': 'Friendship Request Page'
    }
    return render(request, 'friendships/friendship_request.html', context)