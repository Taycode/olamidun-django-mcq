# Generated by Django 2.2.6 on 2020-08-29 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20200829_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
