# Generated by Django 4.2.1 on 2023-05-07 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('split_wise', '0002_rename_user_expense_userexpenseowedby_user_expense_owed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='group_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_expense', to='split_wise.group'),
        ),
    ]
