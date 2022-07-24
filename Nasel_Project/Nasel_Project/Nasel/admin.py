from django.contrib import admin
from .models import CommentModel,ProfileModel,AnimalModel,OrderModel


class profileAdmin(admin.ModelAdmin):
  list_display = ('name','user')
  list_filter = ('user',)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name','age','awards','user')
    list_filter = ('name',)
    search_fields = ['name']

class commentAdmin(admin.ModelAdmin):
    list_display = ('comment','user')
    date_hierarchy = 'created_at'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('Animal','user')
    date_hierarchy = 'date'


admin.site.register(ProfileModel,profileAdmin)
admin.site.register(AnimalModel,AnimalAdmin)
admin.site.register(CommentModel,commentAdmin)
admin.site.register(OrderModel,OrderAdmin)
