from django.contrib import admin
from .models import User, Post

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def password_visibe(self, obj):
        return "*"*len(obj.password)
    list_display = ['username', 'password_visibe']
    # readonly_fields = ('password_visible',)
    


    




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['user', 'title', 'file_field']


# admin.site.register(File)