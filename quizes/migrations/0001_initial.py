# Generated by Django 3.2.6 on 2021-08-31 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='время на прохождение теста')),
                ('required_score_to_pass', models.IntegerField()),
                ('difficluty', models.CharField(choices=[('легко', 'легко'), ('средне', 'средне'), ('сложно', 'сложно')], max_length=6)),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
