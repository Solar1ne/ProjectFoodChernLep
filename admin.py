from django.contrib import admin
from .Models import Dish, Canteen, CReview, DReview, MyUser, DishState

# Register your models here.
admin.site.register(Canteen)
admin.site.register(Dish)
admin.site.register(CReview)
admin.site.register(DReview)
admin.site.register(MyUser)
admin.site.register(DishState)

