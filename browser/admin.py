from django.contrib import admin
# Register your models here.
from browser.models import TitleBasics, TitleAkas, TitleCrew, TitleRatings, TitleEpisode, NameBasics, TitlePrincipals

admin.site.register(TitleBasics)
admin.site.register(TitleAkas)
admin.site.register(TitleCrew)
admin.site.register(TitleRatings)
admin.site.register(TitleEpisode)
admin.site.register(NameBasics)
admin.site.register(TitlePrincipals)
