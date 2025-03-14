# Generated by Django 5.0.9 on 2025-03-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='practice_char',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='PRACTICE_CHAR'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='practice_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='PRACTICE_DT'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='practice_int',
            field=models.IntegerField(blank=True, null=True, verbose_name='PRACTICE_INT'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='primary_key',
            field=models.AutoField(db_column='pk', primary_key=True, serialize=False, verbose_name='pk'),
        ),
    ]
