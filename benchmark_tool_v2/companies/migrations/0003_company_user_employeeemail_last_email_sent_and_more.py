# Generated by Django 5.0.6 on 2024-05-10 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_remove_employee_id_remove_employee_position_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeeemail',
            name='last_email_sent',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
