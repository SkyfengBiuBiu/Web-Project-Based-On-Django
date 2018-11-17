from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from discussions.models import ChatMessage,Discussion
from users.models import CustomUser, CustomUserProfile
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from .forms import DiscussionCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.
def home(request,user_id):
    context = {}
    try:
        uid = user_id
        user_discussions=Discussion.objects.filter(users=uid)
        creator_discussions=Discussion.objects.filter(creator=uid)
        all_discussions = user_discussions|creator_discussions
        context['user_id']=uid
        context['discussions'] = all_discussions
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
        user_discussions = None
    return HttpResponse(render(request, 'discussions/discussion_home.html', context))

# Ajax Post Views

class CreateDiscussionView(generic.CreateView):
    template_name = 'discussions/discussion_create.html'
    form_class = DiscussionCreationForm
    success_url = reverse_lazy('discussions:discussion_home')

    def get_success_url(self):
        id =self.request.user.id
        return reverse_lazy('discussions:discussion_home', kwargs={'user_id': id})

    def form_valid(self, form):
        form.creator=self.request.user
        return super(CreateDiscussionView, self).form_valid(form)



class CreateDoneView(generic.TemplateView):
    template_name = 'discussions/discussion_done.html'



def detail(request,discussion_id):

    if request.method == "GET":

        chat_list = ChatMessage.objects.filter(discussion=discussion_id).order_by('-id')[:10]
        chat_list = reversed(list(chat_list))

        return render(request, 'discussions/discussion_detail.html', {'chat_list':chat_list,\
                                                                      'discussion_id':discussion_id})

    else:

        if request.POST.get('SendOrDelete') == 'send':

            timestamp = request.POST.get('timestamp')
            message_content = request.POST.get('MessageContent')

            discussion = Discussion.objects.get(pk=discussion_id)
            chatmessage = ChatMessage.objects.create(user_id=request.user.id, \
                                                     headline=timestamp, \
                                                     content=message_content)

            discussion.chatMessage.add(chatmessage)

        elif request.POST.get('SendOrDelete') == 'delete':

            discussion = Discussion.objects.get(pk=discussion_id)
            creator_id = discussion.creator

            id = request.POST.get('id')
            user_id = request.POST.get('user_id')


            if request.user.id != creator_id:

                if int(user_id) == request.user.id:

                    ChatMessage.objects.filter(discussion=discussion_id, user_id=user_id, id=id).delete()

            elif request.user.id == creator_id:

                    ChatMessage.objects.filter(discussion=discussion_id, user_id=user_id, id=id).delete()

        return HttpResponseRedirect('/discussions/%s/detail' % discussion_id)











    # try:
    #     discussion = Discussion.objects.get(pk=discussion_id)
    #     chats = discussion.chatMessage.all()
    # except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
    #     discussion = None
    # render(request, 'discussions/discussion_detail.html', {'chats': chats})
    #
    # if request.method == 'POST':
    #     post_type = request.POST.get('post_type')
    #     if post_type == 'send_chat':
    #         new_chat = ChatMessage.objects.create(
    #             content = request.POST.get('content'),
    #             user = request.user,
    #             headline=timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S"),
    #         )
    #         new_chat.save()
    #         return HttpResponse()
    #
    #     elif post_type == 'get_chat':
    #         last_chat_id = int(request.POST.get('last_chat_id'))
    #         chats = discussion.chatMessage
    #         chats = chats.objects.filter(id__gt = last_chat_id)
    #         return render(request, 'discussions/discussion_detail.html', {'chats': chats})
    # else:
    #     raise Http404





@method_decorator(login_required, name='dispatch')
class CustomUserLeaveView(generic.DeleteView):
    template_name = 'users/user_confirm_delete.html'
    pk_url_kwarg = 'user_id'
    model = CustomUser

    def get_success_url(self):
        return reverse_lazy('users:delete_done')


def leave(request,discussion_id,user_id):
    context = {}
    try:
        discussion = Discussion.objects.get(pk=discussion_id)
        user=CustomUser.objects.get(pk=user_id)
        discussion.users.remove(user)
        Discussion.objects.filter(users__isnull=True).delete()
        discussion = Discussion.objects.filter(users=user_id)
        context['user_id'] = user_id
        context['discussions'] = discussion
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
        discussion = None
    return HttpResponse(render(request, 'discussions/discussion_home.html', context))