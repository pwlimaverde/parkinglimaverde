# Generated by Django 2.1.7 on 2019-03-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete='cascade', to='core.Pessoa'),
            preserve_default=False,
        ),
    ]
