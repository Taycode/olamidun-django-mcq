# Generated by Django 2.2.6 on 2020-08-30 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0036_answer_question_useranswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
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
