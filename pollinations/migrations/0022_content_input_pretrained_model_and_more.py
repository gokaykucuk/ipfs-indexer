# Generated by Django 4.0 on 2021-12-28 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollinations', '0021_content_input_content_content_input_frame_step_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='input_pretrained_model',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_temperature',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_use_beam_search',
            field=models.TextField(null=True),
        ),
    ]
