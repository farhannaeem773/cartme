from django.contrib import admin
from .models import Category
from .models import Product
from .models import OrderItem
from .models import Contact
from .models import Order


class AdminCategory(admin.ModelAdmin):
    list_display = ['category_title', 'id', 'created_at' ]

admin.site.register(Category , AdminCategory)

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'id', 'Created_at', 'price', 'category', 'published' ]

admin.site.register(Product , AdminProduct)



class AdminContact(admin.ModelAdmin):
    list_display = ['contact_name', 'id', 'email' ]

admin.site.register(Contact , AdminContact)


class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'Email', 'amount', 'date' ]


admin.site.register(Order, AdminOrder)

class AdminOrderItem(admin.ModelAdmin):
    list_display = ['order', 'price' ]


admin.site.register(OrderItem, AdminOrderItem)


