from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class PurchaseOrder(models.Model):
    contact = models.CharField(max_length=200)
    date = models.DateField()
    delivery_date = models.DateField()
    order_no = models.CharField(max_length=15, unique=True)
    reference = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=100)
    tax = models.CharField(max_length=300)
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.order_no
    
class PurchaseOrderItems(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
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

class PurchaseOrderDeliveryInfo(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=80)
    address = models.CharField(max_length=1000)
    attention = models.CharField(max_length=500)
    telephone = PhoneNumberField()
    instructions = models.CharField(max_length=800)

    def __str__(self):
        return self.address

class PurchaseOrderStatus(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    saved_draft = models.BooleanField(blank=True, null=True)
    saved_draft_at = models.DateTimeField(default=None, blank=True, null=True)
    saved_submitted = models.BooleanField()
    saved_submitted_at = models.DateTimeField()
    approved = models.BooleanField()
    approved_at = models.DateTimeField()

    def __str__(self):
        return "Approved? " + str(self.approved)

