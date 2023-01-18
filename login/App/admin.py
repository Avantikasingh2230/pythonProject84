from django.contrib import admin
from django.contrib import admin

from .models import *

from django.contrib.auth.models import Group
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'full_name',
                    'password',
                    'mobile',
                    'country_code',
                    'address',
                    'picture_profile',
                    'occupation',
                    # 'full_name',
                    'timezone',
                    'is_email_verified',
                    'is_mobile_verified',
                    'user_type',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        ('Permissions', {'fields': ( 'groups',)}),

    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'country_code', 'mobile', 'full_name', 'address', 'occupation', 'picture_profile','password1', 'password2', 'is_staff', 'is_active',),
            },
        ),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    list_display = ("email", "mobile", "full_name", "is_staff")


admin.site.register(UserType)
admin.site.register(about)

admin.site.register(Car)
admin.site.register(Image)
admin.site.register(Venue)
admin.site.register(Catering)
admin.site.register(venuecateringcombined)
admin.site.register(displayImage)
# Register your models here.
admin.site.register(dj)
admin.site.register(dhol)
admin.site.register(musicall)
admin.site.register(portpolio_package)
admin.site.register(Engagement)
admin.site.register(prewedding)
admin.site.register(wedding)
admin.site.register(combined)
admin.site.register(engmakeup)
admin.site.register(preweddingmakeup)
admin.site.register(weddingmakeup)
admin.site.register(allmakeup)
admin.site.register(Notification)
admin.site.register(Profile)