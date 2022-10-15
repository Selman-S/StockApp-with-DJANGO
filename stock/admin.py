from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Firm, Product, Transaction

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Firm)
admin.site.register(Transaction)