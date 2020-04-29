# Generated by Django 3.0.3 on 2020-04-29 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ACC', 'Accounting'), ('ART', 'Art'), ('GPY', 'Art Therapy'), ('BIO', 'Biology'), ('BUS', 'Business Administration'), ('CHE', 'Chemistry'), ('CPY', 'Clinical Psychology'), ('COM', 'Communication'), ('CSC', 'Computer Science'), ('EDU', 'Education'), ('ENG', 'English'), ('TSL', 'English as a Second Language'), ('HSC', 'Health Sciences'), ('HST', 'History'), ('HSP', 'Human Services'), ('KIN', 'Kinesiology'), ('LBS', 'Liberal Studies'), ('MTH', 'Mathematics'), ('PHL', 'Philosophy'), ('PSC', 'Political Science'), ('PSY', 'Psychology'), ('REL', 'Religious Studies'), ('SOC', 'Sociology'), ('SPA', 'Spanish Studies')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.CharField(blank=True, max_length=20)),
                ('tuesday', models.CharField(blank=True, max_length=20)),
                ('wednesday', models.CharField(blank=True, max_length=20)),
                ('thursday', models.CharField(blank=True, max_length=20)),
                ('friday', models.CharField(blank=True, max_length=20)),
                ('saturday', models.CharField(blank=True, max_length=20)),
                ('sunday', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(blank=True, max_length=20)),
                ('semester', models.TextField(blank=True, max_length=10)),
                ('course_number', models.TextField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.FloatField()),
                ('credentials', models.TextField(blank=True, max_length=50)),
                ('method', models.IntegerField(choices=[(1, 'Private'), (2, 'Group'), (3, 'Either')], null=True)),
                ('location', models.IntegerField(choices=[(1, 'School'), (2, 'Anywhere'), (3, 'Other')], null=True)),
                ('description', models.TextField(blank=True, max_length=30)),
                ('rating', models.FloatField(null=True)),
                ('num_of_ratings', models.FloatField(default=0)),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutor_match.Schedule')),
                ('subject', models.ManyToManyField(to='tutor_match.Subject')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubjToDept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_match.Department')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_match.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.FloatField()),
                ('standing', models.IntegerField(choices=[(1, 'Freshman'), (2, 'Sophomore'), (3, 'Junior'), (4, 'Senior'), (5, 'Graduate')], null=True)),
                ('method', models.IntegerField(choices=[(1, 'Private'), (2, 'Group'), (3, 'Either')], null=True)),
                ('location', models.IntegerField(choices=[(1, 'School'), (2, 'Anywhere'), (3, 'Other')], null=True)),
                ('description', models.TextField(blank=True, max_length=30)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_match.Department')),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutor_match.Schedule')),
                ('subject', models.ManyToManyField(to='tutor_match.Subject')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
