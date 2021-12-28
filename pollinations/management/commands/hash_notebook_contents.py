from django.core.management.base import BaseCommand
import hashlib

from pollinations.models import Content


class Command(BaseCommand):
    help = "Merge all text inputs on contents."

    def handle(self, *args, **options):
        for content in Content.objects.all():
            hash_object = hashlib.sha1(content.input_notebook_ipynb.encode("utf-8"))
            content.notebook_hash = hash_object.hexdigest()
            content.save()
            print("Hashed notebook contents {}".format(content.cid))
