from django.contrib import admin
from .models import User,userprofile
from django.contrib.auth.admin import UserAdmin
class CustomeUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter= ()
    fieldsets = ()


# Register your models here.
admin.site.register(User,CustomeUserAdmin)
admin.site.register(userprofile)