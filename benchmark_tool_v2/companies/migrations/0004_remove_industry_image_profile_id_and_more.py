# Generated by Django 5.0.6 on 2024-05-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company_user_employeeemail_last_email_sent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='image_profile_id',
        ),
        migrations.AlterField(
            model_name='company',
            name='image_profile_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
