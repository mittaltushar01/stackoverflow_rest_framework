# Generated by Django 2.2 on 2020-04-27 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('id',)},
        ),
    ]
