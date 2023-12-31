# Generated by Django 4.2.6 on 2023-11-01 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_month_choice_regionmonthlyresult_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmonthlyresult',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='school.region'),
        ),
        migrations.AlterField(
            model_name='regionmonthlyresult',
            name='result',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
