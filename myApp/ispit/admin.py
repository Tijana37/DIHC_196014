from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user_created:
            return True
        return False

admin.site.register(Product, ProductAdmin)

# class ProductCategoryAdmin(admin.StackedInline):
#     model = Product
#     extra = 0
#

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Category, CategoryAdmin)



class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname',]
admin.site.register(Client, ClientAdmin)



admin.site.register(Sale)
