# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# from .models import Merchant
# # from .custom_auth import User

# # Define an inline admin descriptor for MerchantInline model
# # which acts a bit like a singleton
# class MerchantInline(admin.StackedInline):
#     model = Merchant
#     can_delete = False
#     verbose_name_plural = 'merchant'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (MerchantInline, )

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, BaseUserAdmin)