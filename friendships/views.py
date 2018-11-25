from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone

from friendships.models import Friendship, FriendshipRequest
from users.models import CustomUser


# Create your views here.


def home(request, user_id):

    if request.user.id is None:

        return HttpResponseRedirect(reverse_lazy('login'))

    elif request.user.id != user_id:

        return HttpResponseRedirect('/friendships/%s/home/' % request.user.id)

    else:

        if request.method == "GET":

            user_list = CustomUser.objects.all().reverse() #list all users

            return render(request, 'friendships/friendship_home.html', {'user_total_list': user_list,'user_id':user_id})






def request(request, user_id):

    if request.user.id is None:

        return HttpResponseRedirect(reverse_lazy('login'))

    elif request.user.id != user_id:

        return HttpResponseRedirect('/friendships/%s/home/' % request.user.id)

    else:

        if request.method == "GET": #when request is GET, list 3 list: send list, receive list and notification list

            request_sending_list = FriendshipRequest.objects.filter(sender_id=user_id, status=0)
            request_receive_list = FriendshipRequest.objects.filter(recipient_id=user_id, status=0)

            friendship_list_send = Friendship.objects.filter(user1_id=user_id)
            friendship_list_recv = Friendship.objects.filter(user2_id=user_id)
            friendship_list = friendship_list_send | friendship_list_recv #merge list that user1 or user2 is login user

            request_decline_notification_list = FriendshipRequest.objects.filter(sender_id=user_id, status=255)
            notification_cnt = request_decline_notification_list.count()


            return render(request, 'friendships/friendship_request.html', {'request_sending_list':request_sending_list,\
                                                                           'request_receive_list':request_receive_list, \
                                                                           'friendship_list':friendship_list, \
                                                                           'request_decline_notification_list':request_decline_notification_list,\
                                                                           'user_id':user_id,\
                                                                           'notification_cnt':notification_cnt})
        else:

            if request.POST.get('SendOrRecvOrFriendOrNotification') == 'send':

                recipient_id = request.POST.get('recipient_id')
                sender_id = request.POST.get('sender_id')
                FriendshipRequest.objects.filter(sender_id=sender_id, recipient_id=recipient_id, status=0).delete()#'send' POST means delete send request

            elif request.POST.get('SendOrRecvOrFriendOrNotification') == 'receive':

                if request.POST.get('status') == 'accept':

                    recipient_id = request.POST.get('recipient_id')
                    sender_id = request.POST.get('sender_id')
                    timestamp = timezone.now()

                    Friendship.objects.create(user1_id=sender_id, user2_id=recipient_id, date=timestamp)
                    FriendshipRequest.objects.filter(sender_id=sender_id, recipient_id=recipient_id, status=0).update(status=128, date=timestamp)#once accept, update status to 'accept'
                    FriendshipRequest.objects.filter(sender_id=recipient_id, recipient_id=sender_id).delete()#delete reverse request

                elif request.POST.get('status') == 'decline':

                    recipient_id = request.POST.get('recipient_id')
                    sender_id = request.POST.get('sender_id')
                    timestamp = timezone.now()

                    FriendshipRequest.objects.filter(sender_id=sender_id, recipient_id=recipient_id, status=0).update(status=255, date=timestamp)#once decline,update status to 'decline'and timing of decline

            elif request.POST.get('SendOrRecvOrFriendOrNotification') == 'friend':

                user1_id = request.POST.get('user1_id')
                user2_id = request.POST.get('user2_id')
                Friendship.objects.filter(user1_id=user1_id, user2_id=user2_id).delete()
                FriendshipRequest.objects.filter(sender_id=user1_id, recipient_id=user2_id, status=128).delete()#once forming friend from one user, reverse send request will be deleted
                return HttpResponseRedirect(reverse_lazy('profiles:my_home'))

            elif request.POST.get('SendOrRecvOrFriendOrNotification') == 'notification':

                sender_id = request.POST.get('sender_id')
                recipient_id = request.POST.get('recipient_id')
                FriendshipRequest.objects.filter(sender_id=sender_id, recipient_id=recipient_id, status=255).delete()#detele notification

            return HttpResponseRedirect('/friendships/%s/request/' % user_id)




def profile(request, user_id, recipient_id):

    if request.user.id is None:

        return HttpResponseRedirect(reverse_lazy('login'))

    elif request.user.id != user_id:

        return HttpResponseRedirect('/friendships/%s/home/' % request.user.id)

    else:

        if request.method == "GET":

            user_detail = CustomUser.objects.filter(id=recipient_id)
            return render(request, 'friendships/friendship_profile.html', {'user_detail': user_detail, \
                                                                           'recipient_id': recipient_id, \
                                                                           'user_id': user_id})
        else:

            timestamp = timezone.now()
            recipient_id = request.POST.get('recipient_id')
            sender_id = request.POST.get('sender_id')

            re_reqst_chk = FriendshipRequest.objects.filter(sender_id=sender_id, recipient_id=recipient_id, status=0).count()
            friend_chk_p = Friendship.objects.filter(user1_id=sender_id, user2_id=recipient_id).count()
            friend_chk_ = Friendship.objects.filter(user1_id=recipient_id, user2_id=sender_id).count()
            if (re_reqst_chk == 0) and (friend_chk_p == 0) and (friend_chk_ == 0):#if send request have been sent or recipient is friend already, send request can not be sent

                FriendshipRequest.objects.create(sender_id=sender_id, recipient_id=recipient_id, date=timestamp, status=0)

            return HttpResponseRedirect('/friendships/%s/request/' % user_id)
