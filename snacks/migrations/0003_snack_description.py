# Generated by Django 4.2.2 on 2023-06-21 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_rename_reviewer_snack_purchaser_remove_snack_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='description',
            field=models.TextField(default='snack description', max_length=255),
        ),
    ]
