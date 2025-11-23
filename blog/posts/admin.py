from django.contrib import admin
from .models import Category, Topic, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['title', 'short_post', 'topic', 'slug', 'created_by']
    list_display_links = ['title']

    @admin.display(description='Short post version')
    def short_post(self, obj):
        words = obj.text.split()
        if len(words) <= 5:
            return ' '.join(words)
        else:
            return ' '.join(words[:5]) + ' ...'
        


# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
