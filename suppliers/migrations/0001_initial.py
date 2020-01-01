# Generated by Django 3.0.1 on 2020-01-01 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supplier_code', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(default='Ex: Firda Firdaus', max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(default='Ex: +6299999999', max_length=20)),
                ('pic', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
