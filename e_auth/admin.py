from django.contrib import admin
from .models import Profile

admin.site.site_header = "DEVxHUB E-Commerce ADMIN"


class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'image', 'gender', 'address', 'phone', 'date_of_birth', 'father_name', 'mother_name']

    list_display_links = ['user']
