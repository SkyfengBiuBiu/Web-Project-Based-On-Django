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

# Create your views here.
def home(request,user_id):
    context = {}
    uid = user_id
    context['uid'] = uid
    try:
        user_discussions=Discussion.objects.filter(users=uid)
        context['discussions'] = user_discussions
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
        user_discussions = None
    return HttpResponse(render(request, 'discussions/discussion_home.html', context))

class CreateDiscussionView(generic.CreateView):
    template_name = 'discussions/discussion_create.html'
    form_class = DiscussionCreationForm
    success_url = reverse_lazy('discussions:create_done')

    def get_user(self):
        try:
            user = CustomUser.objects.get(pk=1)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
            user = None
        return user

    def form_valid(self, form):
        form.request = self.request
        form.owner=self.request.user
        return super(CreateDiscussionView, self).form_valid(form)



class CreateDoneView(generic.TemplateView):
    template_name = 'discussions/discussion_done.html'

def datail(request,discussion_id):
    if request.method == 'POST':
        post_type = request.POST.get('post_type')
        if post_type == 'send_chat':
            new_chat = ChatMessage.objects.create(
                content = request.POST.get('content'),
                user = request.user,
                headline=timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S"),
            )
            new_chat.save()
            return HttpResponse()

        elif post_type == 'get_chat':
            last_chat_id = int(request.POST.get('last_chat_id'))

            try:
                # urlsafe_base64_decode() decodes to byte string
                uid = urlsafe_base64_decode(discussion_id).decode()
                discussion = Discussion.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
                discussion = None

            chats = discussion.chatMessage
            chats = chats.objects.filter(id__gt = last_chat_id)
            return render(request, 'discussions/discussion_detail.html', {'chats': chats})
    else:
        raise Http404


