# Generated by Django 3.2.8 on 2022-03-31 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Warhouse', models.CharField(max_length=30)),
                ('Number', models.IntegerField()),
            ],
        ),
    ]
