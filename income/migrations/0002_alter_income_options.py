# Generated by Django 4.2.2 on 2023-06-30 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['-date']},
        ),
    ]
