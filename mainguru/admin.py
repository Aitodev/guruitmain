from django.contrib import admin
from .models import Applications, Team, Services


class SubscribeConfig(admin.ModelAdmin):
    fields = ('mail', 'name', 'comment')
    list_display = ('name', 'mail', 'date', 'comment')
    admin.site.register(Applications)


class TeamConfig(admin.ModelAdmin):
    fiels = ('name',
             'img',
             'status',
             'phone',
             'instagram',
             'mail')
    list_display = ('name', 'img', 'status')
    admin.site.register(Team)

class ServicesConfig(admin.ModelAdmin):
    fiels = ('namemain','img', 'price', 'description')
    list_display = ('namemain', 'price')
    admin.site.register(Services)
