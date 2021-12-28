from django.core.management.base import BaseCommand, CommandError
import pandas as pd


class Command(BaseCommand):
    help = "Process the queue."

    def handle(self, *args, **options):
        aryshare_pd = pd.read_json("aryshare_success_latest.json")
