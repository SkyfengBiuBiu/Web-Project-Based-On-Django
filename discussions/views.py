from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from discussions.models import ChatMessage,Discussion
from users.models import CustomUser, CustomUserProfile
from django.core.exceptions import ValidationError

# Create your views here.
def home(request,uidb64):
    try:
        # urlsafe_base64_decode() decodes to byte string
        uid = urlsafe_base64_decode(uidb64).decode()
        user_discussions = CustomUser.objects.get(pk=uid).discussions
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
        user_discussions = None
    return user_discussions

    return render(request, 'discussions/discussion_home.html', {'discussions':user_discussions})

def datail(request,uidb64):
    try:
        # urlsafe_base64_decode() decodes to byte string
        uid = urlsafe_base64_decode(uidb64).decode()
        discussion = Discussion.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
        discussion = None
    return discussion

    chats=discussion.chatMessage

    if request.method == 'POST':
        post_type = request.POST.get('post_type')
        if post_type == 'send_chat':
            new_chat = ChatMessage.objects.create(
                content = request.POST.get('content'),
                user = request.user,
            )
            new_chat.save()
            return HttpResponse()
        elif post_type == 'get_chat':
            last_chat_id = int(request.POST.get('last_chat_id'))
            #print last_chat_id
            chats = ChatMessage.objects.filter(id__gt = last_chat_id)
            return render(request, 'discussions/discussion_detail.html', {'chats': chats})
    else:
        raise Http404
