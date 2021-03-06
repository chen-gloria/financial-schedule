# Generated by Django 3.2.4 on 2021-06-20 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_whom', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('due_date', models.DateField()),
                ('invoice_no', models.CharField(max_length=15, unique=True)),
                ('reference', models.CharField(max_length=200)),
                ('branding', models.CharField(max_length=200)),
                ('total', models.DecimalField(decimal_places=2, max_digits=14)),
                ('currency', models.CharField(max_length=100)),
                ('tax', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_draft', models.BooleanField()),
                ('saved_draft_at', models.DateTimeField()),
                ('saved_submitted', models.BooleanField()),
                ('saved_submitted_at', models.DateTimeField()),
                ('approved', models.BooleanField()),
                ('approved_at', models.DateTimeField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=4, max_digits=16)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('account', models.CharField(max_length=500)),
                ('tax_rate', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=80)),
                ('sub_total', models.DecimalField(decimal_places=4, max_digits=16)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
            ],
        ),
    ]
