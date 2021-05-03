from django.contrib import admin
from .models import Groups, Hints, Hint, Groupsinfo, Others

# Register your models here.

admin.site.register(Groups)
admin.site.register(Hints)
admin.site.register(Hint)
admin.site.register(Groupsinfo)
admin.site.register(Others)
