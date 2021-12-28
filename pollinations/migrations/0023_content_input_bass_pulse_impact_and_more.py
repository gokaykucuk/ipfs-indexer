# Generated by Django 4.0 on 2021-12-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollinations', '0022_content_input_pretrained_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='input_bass_pulse_impact',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_bass_story_speed',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_end_second',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_mids_pulse_impact',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_mids_story_speed',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_smoothing',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_start_second',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_story',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_style_suffix',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_text_prompt_bass',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_text_prompt_mids',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_text_prompt_treble',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_trebles_pulse_impact',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_trebles_story_spee',
            field=models.TextField(null=True),
        ),
    ]
