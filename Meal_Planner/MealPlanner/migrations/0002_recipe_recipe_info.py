# Generated by Django 4.0.2 on 2022-02-22 23:01

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MealPlanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_info',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
