from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import generic

from profiles.models import Post
from users.models import CustomUser

post_page_size = 10
friend_page_size = 10
discussion_page_size = 10
event_page_size = 10


# Profiles Home View
class ProfilesHomeView:

    def get_page_data(self, context, owner):
        # Home Page Owner
        context['owner'] = owner
        # Posts List
        context['post_list'] = self.get_posts(owner)
        # Friends List
        context['friend_list'] = self.get_friends(owner)
        # Discussions List
        context['discussion_list'] = self.get_discussions(owner)
        # Events List
        context['event_list'] = self.get_events(owner)
        return context

    def get_posts(self, user):
        post_list = Post.objects.filter(owner=user)
        paginator = Paginator(post_list, post_page_size)
        return paginator.get_page(1)

    def get_friends(self, user):
        pass

    def get_discussions(self, user):
        pass

    def get_events(self, user):
        pass


@method_decorator(login_required, name='dispatch')
class MyHomeView(ProfilesHomeView, generic.TemplateView):
    template_name = 'profiles/profile_home.html'

    def get_context_data(self, **kwargs):
        context = super(MyHomeView, self).get_context_data(**kwargs)
        owner = self.request.user
        return self.get_page_data(context, owner)


@method_decorator(login_required, name='dispatch')
class VisitingHomeView(ProfilesHomeView, generic.TemplateView):
    template_name = 'profiles/profile_home.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super(VisitingHomeView, self).get_context_data(**kwargs)
        owner = CustomUser.objects.get(pk=kwargs[self.pk_url_kwarg])
        return self.get_page_data(context, owner)


# Ajax Post Views
@method_decorator(login_required, name='dispatch')
class PostCreateView(generic.CreateView):
    # @Todo
    def form_valid(self, form):
        response = super(PostCreateView, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk
            }
            return JsonResponse(data)
        else:
            return response

    def form_invalid(self, form):
        response = super(PostCreateView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


@method_decorator(login_required, name='dispatch')
class PostUpdateView(generic.UpdateView):
    pk_url_kwarg = 'post_id'
    # @Todo
    pass


@method_decorator(login_required, name='dispatch')
class PostDeleteView(generic.DeleteView):
    pk_url_kwarg = 'post_id'
    # @Todo
    pass


@method_decorator(login_required, name='dispatch')
class PostListView(generic.ListView):
    pass


# Ajax Comment Views
@method_decorator(login_required, name='dispatch')
class CommentCreateView(generic.CreateView):
    # @Todo
    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass


@method_decorator(login_required, name='dispatch')
class CommentUpdateView(generic.UpdateView):
    pk_url_kwarg = 'comment_id'
    # @Todo
    pass


@method_decorator(login_required, name='dispatch')
class CommentDeleteView(generic.DeleteView):
    pk_url_kwarg = 'comment_id'
    # @Todo
    pass


@method_decorator(login_required, name='dispatch')
class CommentListView(generic.ListView):
    pass
