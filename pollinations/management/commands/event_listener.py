import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Listen for events and trigger handlers."

    def handle(self, *args, **options):
        cmd = ["ipfs", "--api", "/ip4/65.108.44.19/tcp/5005", "pubsub", "sub", "processing_pollen"]
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
            for line in process.stdout:
                print("read line")
                print(line.decode('utf8'))
