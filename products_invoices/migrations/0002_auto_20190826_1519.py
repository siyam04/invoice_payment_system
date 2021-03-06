# Generated by Django 2.2.1 on 2019-08-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_invoices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-id']},
        ),
    ]
