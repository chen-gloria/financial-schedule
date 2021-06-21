from django.contrib import admin
from .models import Quote, QuoteItems, QuoteStatus
# Register your models here.

admin.site.register(Quote)
admin.site.register(QuoteItems)
admin.site.register(QuoteStatus)
