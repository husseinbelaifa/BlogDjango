from django.contrib import admin
from .models import Posts
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude = ('author','created_at')

admin.site.register(Posts,PostAdmin)
