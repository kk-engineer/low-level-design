# Generated by Django 4.2.1 on 2023-05-07 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('split_wise', '0004_rename_participants_group_members_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='expense',
            unique_together={('name', 'created_by')},
        ),
    ]
