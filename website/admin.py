from django.contrib import admin
from . import models

class Travel_DestinationAdmin(admin.ModelAdmin):
    list_display = ('trip_title','trip_choice','trip_price','trip_days')
    search_fields = ('trip_title ',)
    list_filter = ('trip_choice',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name',)
    search_fields = ('user_name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','user_name','blog_date',)
    search_fields = ('blog_title',)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('gallery_title',)
    list_per_page = 10



admin.site.register(models.Travel_Destination,Travel_DestinationAdmin)
admin.site.register(models.Review,ReviewAdmin)
admin.site.register(models.Blog,BlogAdmin)
admin.site.register(models.Gallery,GalleryAdmin)
