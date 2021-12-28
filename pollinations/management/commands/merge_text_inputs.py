from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import re

from pollinations.models import Task, Content


class Command(BaseCommand):
    help = "Merge all text inputs on contents."

    def handle(self, *args, **options):
        for content in Content.objects.all():
            print("Merging content {}".format(content.cid))
            content.merge_text_inputs()
