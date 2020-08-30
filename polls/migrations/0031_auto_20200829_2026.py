# Generated by Django 2.2.6 on 2020-08-29 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_remove_question_answers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='options',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='answer_question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='questions',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='useranswer',
            old_name='user_answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='useranswer',
            old_name='user_question',
            new_name='question',
        ),
    ]
