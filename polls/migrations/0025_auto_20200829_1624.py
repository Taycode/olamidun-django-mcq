# Generated by Django 2.2.6 on 2020-08-29 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_answers_questions_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]