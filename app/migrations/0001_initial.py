# Generated by Django 5.0.3 on 2024-03-26 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=46)),
                ('color', models.CharField(max_length=48)),
                ('RAM', models.CharField(max_length=24)),
                ('memory', models.CharField(max_length=36)),
                ('price', models.FloatField()),
                ('img_url', models.CharField(max_length=98)),
            ],
        ),
    ]
