# Generated by Django 4.0 on 2021-12-28 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollinations', '0005_pollinationscid_input_fps_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PollinationsCID',
            new_name='Content',
        ),
        migrations.RenameModel(
            old_name='ProcessingQueue',
            new_name='Queue',
        ),
    ]
