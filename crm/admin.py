from django.contrib import admin

from .models import CommentCrm, Order, StatusCrm

# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
