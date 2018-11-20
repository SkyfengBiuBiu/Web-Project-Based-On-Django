from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from discussions.models import ChatMessage, Discussion
from users.models import CustomUser
from .forms import DiscussionCreationForm


# Create your views here.
def home(request, user_id):
    context = {}
    try:
        uid = request.user.id
        user_discussions = Discussion.objects.filter(users=uid)
        creator_discussions = Discussion.objects.filter(creator=uid)
        all_discussions = user_discussions | creator_discussions
        context['user_id'] = uid
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
        id = self.request.user.id
        return reverse_lazy('discussions:discussion_home', kwargs={'user_id': id})

    def form_valid(self, form):
        form.creator = self.request.user
        return super(CreateDiscussionView, self).form_valid(form)


def detail(request, discussion_id):
    if request.method == "GET":

        chat_list = ChatMessage.objects.filter(discussion=discussion_id).order_by('-id')[:10]
        chat_list = reversed(list(chat_list))

        return render(request, 'discussions/discussion_detail.html', {'chat_list': chat_list, \
                                                                      'discussion_id': discussion_id})

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

        if request.is_ajax():
            data = {'success': True}
            return JsonResponse(data)
        return HttpResponseRedirect('/discussions/%s/detail' % discussion_id)


def post(request, discussion_id):
    if request.method == "POST":
        chat_list = ChatMessage.objects.filter(discussion=discussion_id).order_by('-id')[:10]
        chat_list = reversed(list(chat_list))
        data = {'chat_list': chat_list,
                'discussion_id': discussion_id}
        return JsonResponse(data)
    else:
        chat_list = ChatMessage.objects.filter(discussion=discussion_id).order_by('-id')[:10]
        chat_list = reversed(list(chat_list))
        return render(request, 'discussions/chat_message_list.html',
                      context={'chat_list': chat_list, 'discussion_id': discussion_id})


def post_fom(request):
    return render(request, 'discussions/chat_message_form.html')


def leave(request, discussion_id, user_id):
    context = {}
    try:
        discussion = Discussion.objects.get(pk=discussion_id)
        user = CustomUser.objects.get(pk=user_id)
        discussion.users.remove(user)
        Discussion.objects.filter(users__isnull=True).delete()

        if (discussion.creator == user):
            discussion.delete()
        Discussion.objects.filter(users__isnull=True).delete()

        user_discussions = Discussion.objects.filter(users=user_id)
        creator_discussions = Discussion.objects.filter(creator=user_id)
        all_discussions = user_discussions | creator_discussions
        context['user_id'] = user_id
        context['discussions'] = all_discussions
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
        discussion = None
    return HttpResponse(render(request, 'discussions/discussion_home.html', context))
