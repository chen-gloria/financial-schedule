from django.db import models

# Create your models here.

class Invoice(models.Model):
    to_whom = models.CharField(max_length=200)
    date = models.DateField()
    due_date = models.DateField()
    invoice_no = models.CharField(max_length=15, unique=True)
    reference = models.CharField()
    branding = models.CharField()
    currency = models.CharField(max_length=100)
    note = models.CharField(max_length=500)
    total_price = models.DecimalField()
    tax = models.CharField()


class InvoiceItems(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    items = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    quantity = models.IntegerField()
    unit_price = models.DecimalField()
    discount = models.DecimalField()
    account = models.CharField()
    tax_rate = models.CharField()
    region = models.CharField()
    amount = models.IntegerField() # Total

class InvoiceStatus(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    saved_draft = models.BooleanField()
    saved_draft_at = models.DateTimeField()
    saved_submitted = models.BooleanField()
    saved_submitted_at = models.DateTimeField()
    approved = models.BooleanField()
    approved_at = models.DateTimeField()


