from django.contrib import admin
from rango.models import Category, Page

# Define a custom admin class for Page
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Display these columns in the admin panel

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
