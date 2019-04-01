# Generated by Django 2.1.7 on 2019-03-28 04:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190328_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movrotativo',
            old_name='checkin',
            new_name='data_checkin',
        ),
        migrations.AddField(
            model_name='movrotativo',
            name='hora_checkin',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]