# Generated by Django 4.2.2 on 2023-06-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='reviewer',
            new_name='purchaser',
        ),
        migrations.RemoveField(
            model_name='snack',
            name='rating',
        ),
        migrations.AlterField(
            model_name='snack',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
