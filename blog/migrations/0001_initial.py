# Generated by Django 4.2.7 on 2023-12-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('blog_content', models.TextField(verbose_name='Содержимое')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='blog_image/', verbose_name='Превью')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('publication_sign', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('view_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
