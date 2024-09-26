# Generated by Django 5.0.3 on 2024-06-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song', models.FileField(upload_to='song/')),
                ('song_image', models.FileField(upload_to='image/')),
            ],
        ),
    ]