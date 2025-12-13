from django.contrib import admin
from .models import Category, Topic, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['title', 'short_post', 'topic_with_category', 'slug', 'created_by', 'created_at']
    list_display_links = ['title']
    list_filter = ['topic', 'created_by', 'topic__category__name', 'created_at']

    @admin.display(description='Short post version')
    def short_post(self, obj):
        words = obj.text.split()
        if len(words) <= 5:
            return ' '.join(words)
        else:
            return ' '.join(words[:5]) + ' ...'
    
    @admin.display(description='Topic name (Category name)')
    def topic_with_category(self, obj):
        return f'{obj.topic.name} ({obj.topic.category.name})'


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created']
    # można też pobrać tylko id kategorii bez zapytania do tabeli category o pozostałe cechy
    # list_display = ['name', 'category_id', 'created']
    # category__name - to jest model category (bo to klucz obcy do Category)
    # oraz cecha name - wyszukujemy więc zarówno po nazwie dla topic (name) oraz
    # dla nazwy kategorii (category__name)
    search_fields = ['name', 'category__name']
    list_filter = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']


# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
