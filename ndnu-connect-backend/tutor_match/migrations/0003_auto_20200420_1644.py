# Generated by Django 3.0.3 on 2020-04-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_match', '0002_auto_20200420_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='subject',
        ),
        migrations.AddField(
            model_name='tutor',
            name='subject',
            field=models.ManyToManyField(to='tutor_match.Subject'),
        ),
    ]