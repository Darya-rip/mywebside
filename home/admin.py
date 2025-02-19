from django.contrib import admin
from home.models import Setting
from home.models import ContactMessage
from home.models import Language
from home.models import SettingLang

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name','code','status']
    list_filter = ['status']
class SettingLangAdmin(admin.ModelAdmin):
    list_display = ['title','keywords','description','lang']
    list_filter = ['lang']

admin.site.register(Setting)
admin.site.register(ContactMessage)
admin.site.register(Language, LanguageAdmin)
admin.site.register(SettingLang, SettingLangAdmin)

