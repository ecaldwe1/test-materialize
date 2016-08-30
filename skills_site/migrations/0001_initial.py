# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra_credit_tokens', models.IntegerField(default=0)),
                ('manager', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proficiency', models.CharField(max_length=30)),
                ('years_of_experience', models.IntegerField()),
                ('developer', models.ForeignKey(to='skills_site.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCredit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_credited', models.DateField(auto_now_add=True)),
                ('recipient', models.ForeignKey(related_name='extracredit_recipient', to='skills_site.Developer')),
                ('sender', models.ForeignKey(related_name='extracredit_sender', to='skills_site.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('difficulty', models.IntegerField()),
                ('family', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='extracredit',
            name='skill',
            field=models.ForeignKey(related_name='extracredit_skill', to='skills_site.Skill'),
        ),
        migrations.AddField(
            model_name='developerskill',
            name='skill',
            field=models.ForeignKey(to='skills_site.Skill'),
        ),
    ]
