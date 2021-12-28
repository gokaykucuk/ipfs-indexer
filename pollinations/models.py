from django.db import models


# Create your models here.
class PollinationsCID(models.Model):
    cid = models.CharField(max_length=255)
    raw_text_input = models.TextField()
    tags = models.JSONField()
    text_output = models.TextField()
    notebook_name = models.TextField()
    # Splatted Fields
    output_gpu = models.TextField(null=True)
    output_gpu_memory = models.TextField(null=True)
    output_run_count = models.IntegerField(null=True)
    output_status = models.TextField(null=True)
    output_success = models.TextField(null=True)
    output_done = models.TextField(null=True)
    output_log = models.TextField(null=True)
    # Input Fields
    input_fps = models.IntegerField(null=True)
    input_social = models.TextField(null=True)
    input_style = models.TextField(null=True)
    input_resolution = models.TextField(null=True)
    input_height = models.IntegerField(null=True)
    input_width = models.IntegerField(null=True)
    input_iterations = models.IntegerField(null=True)
    step_size = models.TextField(null=True)
    input_super_resolution = models.TextField(null=True)

    input_notebook_ipynb = models.TextField(null=True)


class ProcessingQueue(models.Model):
    cid = models.CharField(max_length=255)
    processing_started_at = models.DateTimeField(null=True)
    processed_at = models.DateTimeField(null=True)
