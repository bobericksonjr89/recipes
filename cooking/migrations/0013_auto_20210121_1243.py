# Generated by Django 3.1.1 on 2021-01-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0012_delete_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
