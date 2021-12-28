from django.core.management.base import BaseCommand
from time import sleep

import ipfshttpclient

from pollinations.models import Task

client = ipfshttpclient.connect(
    '/ip4/65.108.44.19/tcp/4005/p2p/12D3KooWLWjqSrwsFJhqMtPAFTZJJFLntYD4njS68co9ZHKXzgEx')


class Command(BaseCommand):
    help = "Listen for events and trigger handlers."

    def handle(self, *args, **options):
        while True:
            sleep(0.5)
            with client.pubsub.subscribe("processing_pollen") as sub:
                for message in sub:
                    Task.objects.create(cid=message)
