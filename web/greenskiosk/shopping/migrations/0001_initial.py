# Generated by Django 3.1.1 on 2020-09-10 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('catalogue', '0002_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('date_placed', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('delivery_time', models.DateTimeField()),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_of_Payment', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.order')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(max_length=50)),
                ('products', models.ManyToManyField(to='catalogue.Product')),
            ],
        ),
    ]