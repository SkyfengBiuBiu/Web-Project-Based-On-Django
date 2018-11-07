from django.shortcuts import render,redirect


def EventHomeView(request, user_id):

    if request.method == "GET" and user_id == 1:
        return redirect('http://map.google.com')

    else:
        return render(request, 'event_home.html')


def EventDetailView(request, event_id):

    if request.method == "GET" and event_id == 2:
        return redirect('http://map.google.com')

    else:
        return render(request, 'event_detail.html')


def EventInvitationView(request, user_id):

    if request.method == "GET" and user_id == 3:
        return redirect('http://map.google.com')

    else:
        return render(request, 'event_invitation.html')