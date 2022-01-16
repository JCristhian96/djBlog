from atexit import register
from django.contrib import admin
# Models
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title', 'created_at')