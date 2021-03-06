# Generated by Django 3.1 on 2020-08-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the hero', max_length=200)),
                ('description', models.TextField(help_text='Describe the individual')),
                ('power_type', models.CharField(max_length=50)),
                ('strength', models.IntegerField(help_text='A score between 0 and 10')),
                ('durability', models.IntegerField(help_text='A score between 0 and 10')),
                ('intelligence', models.IntegerField(help_text='A score between 0 and 10')),
                ('fighting_ability', models.IntegerField(help_text='A score between 0 and 10')),
                ('tech', models.IntegerField(help_text='A score between 0 and 10')),
                ('sanity', models.IntegerField(help_text='A score between 0 and 10')),
                ('xFactor', models.IntegerField(help_text='A score between 0 and 10')),
            ],
        ),
    ]
