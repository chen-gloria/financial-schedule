# Generated by Django 3.2.4 on 2021-06-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderstatus',
            name='saved_draft',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorderstatus',
            name='saved_draft_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
