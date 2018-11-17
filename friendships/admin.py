from django.contrib import admin


from friendships.models import Friendship,FriendshipRequest


# Register your models here.


class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'date')


admin.site.register(Friendship, FriendshipAdmin)





class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'status', 'date')


admin.site.register(FriendshipRequest, FriendshipRequestAdmin)