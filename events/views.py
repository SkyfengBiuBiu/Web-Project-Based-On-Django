from django.shortcuts import render,redirect

# from events import models

def EventHomeView(request, user_id):

    event_list = {
                    '1': [{'event_id': 1, 'event_name': 'hello',    'user_id': user_id},
                          {'event_id': 2, 'event_name': 'world',    'user_id': user_id},
                          {'event_id': 3, 'event_name': 'darling',  'user_id': user_id}],
                    '2': [{'event_id': 1, 'event_name': 'you',      'user_id': user_id},
                          {'event_id': 2, 'event_name': 'are',      'user_id': user_id},
                          {'event_id': 3, 'event_name': 'smart',    'user_id': user_id}],
                    '3': [{'event_id': 1, 'event_name': 'I',        'user_id': user_id},
                          {'event_id': 2, 'event_name': 'know',     'user_id': user_id},
                          {'event_id': 3, 'event_name': 'you',      'user_id': user_id}],
                    '4': [{'event_id': 1, 'event_name': 'can',      'user_id': user_id},
                          {'event_id': 2, 'event_name': 'do',       'user_id': user_id},
                          {'event_id': 3, 'event_name': 'it',       'user_id': user_id}],
                    '5': [{'event_id': 1, 'event_name': 'yes',      'user_id': user_id},
                          {'event_id': 2, 'event_name': 'I',        'user_id': user_id},
                          {'event_id': 3, 'event_name': 'do',       'user_id': user_id}],
                  };


    if request.method == "GET":
        return render(request, 'event_home.html', {'event_list': event_list[str(user_id)]})
    else:
        return redirect('http://www.nba.com')


def EventDetailView(request, event_id):

    detail_list = {
                    '1': [{'time': '11:00', 'member_name': 'Li Lei',     'location': 'Mokontalo'},
                          {'time': '12:00', 'member_name': 'Han Mei',    'location': 'Konetalo'},
                          {'time': '13:00', 'member_name': 'Wang Cai',   'location': 'TIETOTALO'}],
                    '2': [{'time': '14:00', 'member_name': 'Lai Fu',     'location': 'Mokontalo'},
                          {'time': '15:00', 'member_name': 'A Huang',    'location': 'Konetalo'},
                          {'time': '16:00', 'member_name': 'Xiao Qiang', 'location': 'TIETOTALO'}],
                    '3': [{'time': '17:00', 'member_name': 'Gou Dan',    'location': 'Mokontalo'},
                          {'time': '18:00', 'member_name': 'Cui Hua',    'location': 'Konetalo'},
                          {'time': '19:00', 'member_name': 'Tie Zhu',    'location': 'TIETOTALO'}],
                  };


    if request.method == "GET":
        return render(request, 'event_detail.html', {'detail_list': detail_list[str(event_id)]})

    else:
        return redirect('http://map.google.com')


def EventInvitationView(request, user_id):

    invitation_list = {
                    '1': [{'inviter_name': 'Li Lei',     'reason': 'basketball', 'location': 'Mokontalo'},
                          {'inviter_name': 'Han Mei',    'reason': 'sing',       'location': 'Konetalo'},
                          {'inviter_name': 'Wang Cai',   'reason': 'football',   'location': 'TIETOTALO'}],
                    '2': [{'inviter_name': 'Lai Fu',     'reason': 'shopping',   'location': 'Mokontalo'},
                          {'inviter_name': 'A Huang',    'reason': 'swimming',   'location': 'Konetalo'},
                          {'inviter_name': 'Xiao Qiang', 'reason': 'skiing',     'location': 'TIETOTALO'}],
                    '3': [{'inviter_name': 'Gou Dan',    'reason': 'game',       'location': 'Mokontalo'},
                          {'inviter_name': 'Cui Hua',    'reason': 'eating',     'location': 'Konetalo'},
                          {'inviter_name': 'Tie Zhu',    'reason': 'chat',       'location': 'TIETOTALO'}],
                  };

    if request.method == "GET":
        return render(request, 'event_invitation.html', {'invitation_list': invitation_list[str(user_id)]})

    else:
        return redirect('http://www.facebook.com')


