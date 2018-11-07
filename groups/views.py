from django.shortcuts import render,redirect


def GroupHomeView(request, user_id):

    if request.method == "GET" and user_id == 5:
        return redirect('http://map.google.com')

    else:
        return render(request, 'group_home.html')




def GroupDetailView(request, group_id):

    if request.method == "GET" and group_id  == 7:
        return redirect('http://www.facebook.com')

    else:
        return render(request, 'group_detail.html')



