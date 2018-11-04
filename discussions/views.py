from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'content': 'Disussions Home Page'
    }
    return render(request, 'discussions/discussion_home.html', context)

def datail(request):
    context = {
        'content': 'Discussions Detail Page'
    }
    return render(request, 'discussions/discussion_detail.html', context)