from django.shortcuts import render,redirect

from groups import models

def GroupHomeView(request, user_id):

    group_list = {
                    '1': [{'group_id': 1, 'group_name': 'hello',    'user_id': user_id},
                          {'group_id': 2, 'group_name': 'world',    'user_id': user_id},
                          {'group_id': 3, 'group_name': 'darling',  'user_id': user_id}],
                    '2': [{'group_id': 1, 'group_name': 'you',      'user_id': user_id},
                          {'group_id': 2, 'group_name': 'are',      'user_id': user_id},
                          {'group_id': 3, 'group_name': 'smart',    'user_id': user_id}],
                    '3': [{'group_id': 1, 'group_name': 'I',        'user_id': user_id},
                          {'group_id': 2, 'group_name': 'know',     'user_id': user_id},
                          {'group_id': 3, 'group_name': 'you',      'user_id': user_id}],
                    '4': [{'group_id': 1, 'group_name': 'can',      'user_id': user_id},
                          {'group_id': 2, 'group_name': 'do',       'user_id': user_id},
                          {'group_id': 3, 'group_name': 'it',       'user_id': user_id}],
                    '5': [{'group_id': 1, 'group_name': 'yes',      'user_id': user_id},
                          {'group_id': 2, 'group_name': 'I',        'user_id': user_id},
                          {'group_id': 3, 'group_name': 'do',       'user_id': user_id}],
                  };


    if request.method == "GET":
            return render(request, 'group_home.html', {'group_list': group_list[str(user_id)]})
    else:
        if request.POST.get('group_id') == '1':
            return redirect('http://map.google.com')
        elif request.POST.get('group_id') == '2':
            return redirect('http://www.baidu.com')
        else:
            return redirect('http://www.nba.com')





def GroupDetailView(request, group_id):


    member_list = {
                    '1': [{'member_id': 1, 'member_name': 'Li Lei'},
                          {'member_id': 2, 'member_name': 'Han Mei'},
                          {'member_id': 3, 'member_name': 'Wang Cai'}],
                    '2': [{'member_id': 1, 'member_name': 'Lai Fu'},
                          {'member_id': 2, 'member_name': 'A Huang'},
                          {'member_id': 3, 'member_name': 'Xiao Qiang'}],
                    '3': [{'member_id': 1, 'member_name': 'Gou Dan'},
                          {'member_id': 2, 'member_name': 'Cui Hua'},
                          {'member_id': 3, 'member_name': 'Tie Zhu'}],
                  };



    if request.method == "GET" :
        return render(request, 'group_detail.html',{'member_list': member_list[str(group_id)]})
    else:
        return redirect('http://www.facebook.com')



