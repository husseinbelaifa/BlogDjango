from django.contrib import admin
from .models import Posts
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude = ('author','created_at')

    def save_model(self, request, obj, form, change):
        obj.author=request.user
        obj.save()
        # return super().save_model(request, obj, form, change)

    
admin.site.register(Posts,PostAdmin)
