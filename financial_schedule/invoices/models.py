from django.db import models

# Create your models here.

class Invoice(models.Model):
    to_whom = models.CharField(max_length=200)
    date = models.DateField()
    due_date = models.DateField()
    invoice_no = models.CharField(max_length=15, unique=True)
    reference = models.CharField(max_length=200)
    branding = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=100)
    tax = models.CharField(max_length=300)
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.to_whom
    
class InvoiceItems(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
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

class InvoiceStatus(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    saved_draft = models.BooleanField(blank=True, null=True)
    saved_draft_at = models.DateTimeField(default=None, blank=True, null=True)
    saved_submitted = models.BooleanField()
    saved_submitted_at = models.DateTimeField()
    approved = models.BooleanField()
    approved_at = models.DateTimeField()

    def __str__(self):
        return "Approved? " + str(self.approved)


