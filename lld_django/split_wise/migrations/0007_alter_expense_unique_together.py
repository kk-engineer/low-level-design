# Generated by Django 4.2.1 on 2023-05-07 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('split_wise', '0006_rename_group_name_expense_group_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='expense',
            unique_together={('name', 'created_by', 'group_id')},
        ),
    ]
