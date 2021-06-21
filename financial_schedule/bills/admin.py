from django.contrib import admin
from .models import Bill, BillItems, BillStatus
# Register your models here.

admin.site.register(Bill)
admin.site.register(BillItems)
admin.site.register(BillStatus)

