from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'content': 'Profile Home Page'
    }
    return render(request, 'profiles/profile_home.html', context)
