from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import re

from pollinations.models import Task


class Command(BaseCommand):
    help = "Insert the products from a csv file."

    def handle(self, *args, **options):
        twitter_pd = pd.read_csv("data/pollinations_ai_user_tweets.csv")
        unique_post_texts = twitter_pd["URLs"].dropna().unique()

        full_text = "".join(unique_post_texts)
        cid_numbers = re.findall("Qm[1-9A-Za-z]{44}[^OIl]", full_text)
        cid_numbers_series = pd.Series(cid_numbers)
        cid_numbers_series = cid_numbers_series.str.replace("/", "")
        unique_cids = cid_numbers_series.unique()
        print(f"{len(unique_cids)} CIDs found.")
        for cid in unique_cids:
            try:
                Task.objects.create(cid=cid)
            except:
                pass
        self.stdout.write(self.style.SUCCESS("Successfully imported products"))
