from django.core.management.base import BaseCommand
from time import sleep

import ipfshttpclient

from pollinations.models import Task

client = ipfshttpclient.connect('/dns/ipfs.pollinations.ai/tcp/5005/http')


class Command(BaseCommand):
    help = "Listen for events and trigger handlers."

    def handle(self, *args, **options):
        while True:
            sleep(0.5)
            with client.pubsub.subscribe("processing_pollen") as sub:
                for message in sub:
                    Task.objects.create(cid=message)
