# Generated by Django 2.2.6 on 2020-08-28 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200828_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='options_text',
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options_text', models.CharField(max_length=200)),
                ('question_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]