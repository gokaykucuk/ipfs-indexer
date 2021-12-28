from concurrent.futures import ThreadPoolExecutor

from django.core.management.base import BaseCommand

from pollinations.adapter import process_cid
from pollinations.models import Task


class Command(BaseCommand):
    help = "Process the queue."

    @staticmethod
    def process_next_cid():
        next_task = Task.objects.filter(state_updates=[]).first()
        if next_task is None:
            return None

        next_task.add_state_update("started_processing")
        next_task.save()
        print("Processing {}".format(next_task.cid))
        run_result = process_cid(next_task)
        next_task.add_state_update("finished_processing")
        return run_result

    def handle(self, *args, **options):
        with ThreadPoolExecutor(max_workers=10) as executor:
            while True:
                future = executor.submit(self.process_next_cid)
                print(future.result())
