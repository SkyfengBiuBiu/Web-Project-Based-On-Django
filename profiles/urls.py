from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.MyHomeView.as_view(), name='my_home'),
    path('<int:user_id>/home/', views.VisitingHomeView.as_view(), name='visit_home'),

    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:user_id>/list/<int:page_no>/', views.PostListView.as_view(), name='post_list'),

    path('comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:comment_id>/update', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:comment_id>/delete', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:post_id>/list/', views.CommentListView.as_view(), name='comment_list')
]
