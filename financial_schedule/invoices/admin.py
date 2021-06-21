from django.contrib import admin
from .models import Invoice, InvoiceItems, InvoiceStatus
# Register your models here.

admin.site.register(Invoice)
admin.site.register(InvoiceItems)
admin.site.register(InvoiceStatus)
