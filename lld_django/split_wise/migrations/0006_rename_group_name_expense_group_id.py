# Generated by Django 4.2.1 on 2023-05-07 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('split_wise', '0005_alter_expense_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='group_name',
            new_name='group_id',
        ),
    ]
