from django.contrib import admin

# Register your models here.
from ecartapp.models import  Category,Product

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug','desc']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','updated','created']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock','available']
    list_per_page = 20
admin.site.register(Product,productadmin)