# Generated by Django 4.1.4 on 2023-01-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_remove_preferences_preference_id_preferences_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flagged',
            name='preference',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flagged',
            name='work_done',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='breaks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='calls',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='emails',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='hours',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='meetings',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workdone',
            name='breaks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workdone',
            name='calls',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workdone',
            name='emails',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workdone',
            name='hours',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workdone',
            name='meetings',
            field=models.IntegerField(),
        ),
    ]