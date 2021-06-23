# Generated by Django 3.2.4 on 2021-06-22 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Текст ответа')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг ответа')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания ответа')),
                ('is_marked_correct', models.BooleanField(default=False, verbose_name='Отмечен ли как верный')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30, verbose_name='Ник пользователя')),
                ('profile_pic', django_resized.forms.ResizedImageField(crop=None, default='avatars/default_pic.png', force_format=None, keep_meta=True, quality=100, size=[50, 64], upload_to='avatars/%Y/%m/%d', verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок вопроса')),
                ('content', models.TextField(verbose_name='Текст вопроса')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг вопроса')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания вопроса')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, unique=True, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=0, verbose_name='Поставленная оценка')),
                ('related_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_votes', to='app.question', verbose_name='Оцениваемый вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Кто оценил')),
            ],
            options={
                'verbose_name': 'Оценка вопроса',
                'verbose_name_plural': 'Оценки вопросов',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', related_query_name='question', to='app.Tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='voted_questions', related_query_name='voted_questions', through='app.QuestionVote', to='app.Profile', verbose_name='Оценки вопроса'),
        ),
        migrations.CreateModel(
            name='AnswerVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=0, verbose_name='Поставленная оценка')),
                ('related_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_votes', to='app.answer', verbose_name='Оцениваемый ответ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Кто оценил')),
            ],
            options={
                'verbose_name': 'Оценка ответа',
                'verbose_name_plural': 'Оценки ответов',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='related_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', related_query_name='answer', to='app.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='voted_answers', related_query_name='voted_answer', through='app.AnswerVote', to='app.Profile', verbose_name='Оценки вопроса'),
        ),
    ]
