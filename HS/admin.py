from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .forms import UserCreationForm
from .models import User

# Register your models here.
admin.site.register(Assignment)
admin.site.register(class_2_1)
admin.site.register(class_2_2)
admin.site.register(class_2_3)
admin.site.register(class_2_4)
admin.site.register(class_2_5)
admin.site.register(class_2_6)

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserCreationForm

    list_display = ('name', 'student_id', 'email','is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('id', 'password')}),
        (_('Personal info'), {'fields': ('name', 'email', 'student_id')}),
        (_('Permissions'), {'fields': ('is_superuser',)}),
    )
    search_fields = ('email', 'name', 'id')
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
        # list_display_links = (
        #     'id',
        # )
