# Generated by Django 2.2.6 on 2020-08-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20200829_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]
