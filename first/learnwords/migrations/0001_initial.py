# Generated by Django 3.2.8 on 2021-11-13 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Почта')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_language', models.CharField(default='', max_length=20)),
                ('second_language', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/words/')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='learnwords.user')),
            ],
        ),
    ]
