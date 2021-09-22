from django.contrib import admin

from .models import CommentCrm, Order, StatusCrm

# Register your models here.
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('order_id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('order_id', 'order_name')
    search_fields = ('order_id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    list_per_page = 5
    list_max_show_all = 100
    fields = ('order_id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('order_id', 'order_dt')
    inlines = [Comment,]


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
