from django.contrib import admin

from main.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'year',)


admin.site.register(Purpose)
admin.site.register(Type_of)
admin.site.register(Family)
admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Rating)
admin.site.register(Volume)
admin.site.register(Brand)
