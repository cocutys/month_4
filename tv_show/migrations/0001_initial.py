# Generated by Django 4.1.4 on 2022-12-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('genre', models.CharField(choices=[('Detective', 'Detective'), ('Horror', 'Horror'), ('Anime', 'Anime'), ('Comedy', 'Comedy'), ('Document', 'Document'), ('Fantasy', 'Fantasy')], max_length=100)),
            ],
        ),
    ]
