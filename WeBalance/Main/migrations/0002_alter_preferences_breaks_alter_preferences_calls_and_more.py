# Generated by Django 4.1.4 on 2023-01-02 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0001_initial'),
    ]

    operations = [
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
            field=models.IntegerField(choices=[(1, 'Less Than Twenty'), (2, 'Twenty To Forty'), (3, 'Morethanfourty')]),
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
        migrations.CreateModel(
            name='WorkDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('emails', models.IntegerField()),
                ('calls', models.IntegerField()),
                ('hours', models.IntegerField()),
                ('meetings', models.IntegerField()),
                ('breaks', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]