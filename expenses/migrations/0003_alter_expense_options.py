# Generated by Django 4.2.2 on 2023-06-30 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_rename_expenses_expense'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
    ]