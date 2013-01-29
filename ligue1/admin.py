from django.contrib import admin

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'budget', 'points')


from ligue1.models import Club
admin.site.register(Club)


