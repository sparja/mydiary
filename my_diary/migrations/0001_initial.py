# Generated by Django 4.2.2 on 2024-09-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('descriptions', models.CharField(blank=True, max_length=200, null=True, verbose_name='описание')),
                ('text_diary', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='diary/photo', verbose_name='картинка')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='дата обновления')),
            ],
            options={
                'verbose_name': 'Дневник',
                'verbose_name_plural': 'Дневники',
            },
        ),
    ]
