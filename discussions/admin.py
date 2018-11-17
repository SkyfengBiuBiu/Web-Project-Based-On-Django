from django.contrib import admin
from django.contrib import admin

from discussions.models import Discussion,ChatMessage
# Register your models here.
class DiscussionAdmin(admin.ModelAdmin):
    exclude = ('date',)
    list_display = ('topic', 'creator')

class ChatMessageAdmin(admin.ModelAdmin):
    exclude = ('headline',)
    list_display = ('user', 'content')

admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)