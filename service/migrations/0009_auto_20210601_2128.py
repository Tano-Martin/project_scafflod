# Generated by Django 3.2 on 2021-06-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_prestation_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advantage',
            name='pack',
        ),
        migrations.AddField(
            model_name='pack',
            name='advantage',
            field=models.ManyToManyField(related_name='advantage_pack', to='service.Advantage'),
        ),
    ]
