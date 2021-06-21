from django.contrib import admin
from .models import PurchaseOrder, PurchaseOrderItems, PurchaseOrderDeliveryInfo, PurchaseOrderStatus
# Register your models here.

admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItems)
admin.site.register(PurchaseOrderDeliveryInfo)
admin.site.register(PurchaseOrderStatus)
