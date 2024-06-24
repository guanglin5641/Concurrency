from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Variant

class ProductVariantInline(admin.TabularInline):
    model = Variant
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline]

admin.site.register(Product, ProductAdmin)


