# Generated by Django 2.2 on 2020-09-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindful_api', '0003_auto_20200917_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_active',
            field=models.DateTimeField(null=True),
        ),
    ]
