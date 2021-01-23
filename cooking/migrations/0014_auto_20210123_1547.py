# Generated by Django 3.1.1 on 2021-01-23 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0013_auto_20210121_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='side',
        ),
        migrations.AddField(
            model_name='menu',
            name='side1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='side1_recipe', to='cooking.recipeitem'),
        ),
        migrations.AddField(
            model_name='menu',
            name='side2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='side2_recipe', to='cooking.recipeitem'),
        ),
        migrations.AddField(
            model_name='menu',
            name='side3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='side3_recipe', to='cooking.recipeitem'),
        ),
    ]