# Generated by Django 4.0 on 2021-12-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollinations', '0013_content_input_audio_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='input_model_type',
            field=models.TextField(null=True),
        ),
    ]
