from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from profiles.forms import PostForm
from profiles.models import Post
from users.models import CustomUser

post_page_size = 5
friend_page_size = 10
discussion_page_size = 10
event_page_size = 10


# Profiles Home View
class ProfilesHomeView:

    def get_page_data(self, context, owner):
        # Home Page Owner
        context['owner'] = owner
        # Posts List
        context['post_list'] = self.get_posts(owner, 1)
        # Friends List
        context['friend_list'] = self.get_friends(owner)
        # Discussions List
        context['discussion_list'] = self.get_discussions(owner)
        # Events List
        context['event_list'] = self.get_events(owner)
        return context

    def get_posts(self, user, page_no):
        post_list = Post.objects.filter(owner=user)
        paginator = Paginator(post_list, post_page_size)
        return paginator.get_page(page_no)

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
    template_name = 'profiles/post/post_create_form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('profiles:my_home')

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(PostCreateView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('profiles:my_home'))

    def form_valid(self, form):
        if self.request.is_ajax():
            form.owner = self.request.user
            response = super(PostCreateView, self).form_valid(form)
            data = {
                'message': 'You have made a new posts.'
            }
            return JsonResponse(data)
        else:
            return HttpResponseRedirect(reverse_lazy('profiles:my_home'))

    def form_invalid(self, form):
        if self.request.is_ajax():
            response = super(PostCreateView, self).form_invalid(form)
            return JsonResponse(form.errors, status=400)
        else:
            return HttpResponseRedirect(reverse_lazy('profiles:my_home'))


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
class PostListView(ProfilesHomeView, generic.ListView):
    template_name = 'profiles/post/post_list.html'
    pk_url_kwarg = 'user_id'
    page_kwarg = 'page_no'
    model = Post

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(PostListView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('profiles:my_home'))

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        owner = CustomUser.objects.get(pk=self.kwargs[PostListView.pk_url_kwarg])
        page_no = self.kwargs[PostListView.page_kwarg]
        context['post_list'] = self.get_posts(owner, page_no)
        return context


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
