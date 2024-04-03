from django.contrib import admin
from techapp.models import laptop
# Register your models here.
class adminlaptop(admin.ModelAdmin):
    list_display=['id','Name','type','model','colour','price']
    list_filter=['type','model']
admin.site.register(laptop,adminlaptop)