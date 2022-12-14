# Generated by Django 4.1.2 on 2022-10-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ManyToManyField(to='users.location', verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'Пользователь'), ('admin', 'Администратор'), ('moderator', 'Модератор')], default='member', max_length=16, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Никнейм'),
        ),
    ]
