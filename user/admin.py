from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from user.models import User


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('password',
                           'last_login',
                           'is_superuser',
                           'groups',
                           'user_permissions',
                           'username',
                           'email',
                           'is_staff',
                           'is_active',
                           'date_joined',
                           'is_clinic',
                           'is_patient')}),
    )


admin.site.register(User, UserAdmin)
