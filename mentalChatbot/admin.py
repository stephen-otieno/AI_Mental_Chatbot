from django.contrib import admin
from mentalChatbot.models import Client, ForumPost, ForumResponse


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    actions = ['approve_posts']  # Add this action

    def approve_posts(self, request, queryset):
        """Mark selected posts as approved"""
        queryset.update(is_approved=True)
    approve_posts.short_description = "Approve selected posts"


@admin.register(ForumResponse)
class ForumResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'post', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    actions = ['approve_responses']  # Add bulk approval action for responses

    def approve_responses(self, request, queryset):
        """Mark selected responses as approved"""
        queryset.update(is_approved=True)
    approve_responses.short_description = "Approve selected responses"


admin.site.register(Client)



# Register your models here.
