from django.contrib import admin
from home.models import Setting
from home.models import ContactMessage
from home.models import Language

# Register your models here.


admin.site.register(Setting)
admin.site.register(ContactMessage)
admin.site.register(Language)

