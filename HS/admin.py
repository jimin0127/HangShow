from django.contrib import admin
from .models import Assignment, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
admin.site.register(Assignment)

# Register your models here.
class UserAdmin(BaseUserAdmin):
    @admin.register(User)
    class UserAdmin(admin.ModelAdmin):
        list_display = (
            'id',
            'name',
            'student_id',
        )

        list_display_links = (
            'id',
        )
