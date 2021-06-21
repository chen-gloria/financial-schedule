from django.db import models

# Create your models here.

class Quote(models.Model):
    customer = models.CharField(max_length=200)
    date = models.DateField()
    expiry_date = models.DateField()
    quote_no = models.CharField(max_length=15, unique=True)
    reference = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=100)
    tax = models.CharField(max_length=300)
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.quote_no
    
class QuoteItems(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    items = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=16, decimal_places=4)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    account = models.CharField(max_length=500)
    tax_rate = models.CharField(max_length=200)
    region = models.CharField(max_length=80)
    sub_total = models.DecimalField(max_digits=16, decimal_places=4)

    def __str__(self):
        return self.items

class QuoteStatus(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    saved_draft = models.BooleanField(blank=True, null=True)
    saved_draft_at = models.DateTimeField(default=None, blank=True, null=True)
    sent = models.BooleanField()
    sent_at = models.DateTimeField()

    def __str__(self):
        return "Sent? " + str(self.sent)


