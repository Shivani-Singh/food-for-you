from django.contrib import admin
from .models import User, Restaurant, Menus, Items, JoinTable, Orders, Cart, ManageOrder

# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Menus)
admin.site.register(Items)
admin.site.register(JoinTable)
admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(ManageOrder)