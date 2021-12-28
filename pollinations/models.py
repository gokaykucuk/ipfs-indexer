import datetime

from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class Content(models.Model):
    cid = models.CharField(max_length=255, unique=True)
    raw_text_input = models.TextField()
    tags = models.JSONField(null=True)
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

    input_image_file = models.TextField(null=True)

    input_width = models.IntegerField(null=True)
    input_iterations = models.IntegerField(null=True)
    input_step_size = models.TextField(null=True)
    input_super_resolution = models.TextField(null=True)

    input_notebook_ipynb = models.TextField(null=True)
    input_text_input = models.TextField(null=True)
    input_fix_camera = models.TextField(null=True)
    input_image_prompt_file = models.TextField(null=True)
    input_images_prompt_weight = models.TextField(null=True)
    input_learning_rate = models.TextField(null=True)
    input_seed = models.TextField(null=True)
    input_steps = models.TextField(null=True)
    input_input_text_prompt_weight = models.TextField(null=True)
    input_models = models.TextField(null=True)
    input_speed = models.TextField(null=True)
    input_text_prompt = models.TextField(null=True)
    input_audio_file = models.TextField(null=True)
    input_motion_randomness = models.TextField(null=True)
    input_motion_react = models.TextField(null=True)
    input_motion_react_to = models.TextField(null=True)
    input_pulse_react = models.TextField(null=True)
    input_pulse_react_to = models.TextField(null=True)
    input_truncation = models.TextField(null=True)
    input_model_type = models.TextField(null=True)
    input_model = models.TextField(null=True)
    input_batch_size = models.TextField(null=True)
    input_prompt = models.TextField(null=True)
    input_all_title = models.TextField(null=True)
    input_choose_diffusion_model = models.TextField(null=True)
    input_cut_batches = models.TextField(null=True)
    input_cut_pow = models.TextField(null=True)
    input_cutn = models.TextField(null=True)
    input_imageHeight = models.TextField(null=True)
    input_imageWidth = models.TextField(null=True)
    input_init_weight_mse = models.TextField(null=True)
    input_resSize = models.TextField(null=True)
    input_starting_noise = models.TextField(null=True)
    input_youtube_dl_link = models.TextField(null=True)
    input_upscale_factor = models.TextField(null=True)
    input_video_file = models.TextField(null=True)
    input_diffusion_model = models.TextField(null=True)
    input_content = models.TextField(null=True)
    input_frame_step = models.TextField(null=True)
    input_method = models.TextField(null=True)
    input_sideX = models.TextField(null=True)
    input_sideY = models.TextField(null=True)
    input_translate = models.TextField(null=True)
    input_pretrained_model = models.TextField(null=True)
    input_temperature = models.TextField(null=True)
    input_use_beam_search = models.TextField(null=True)
    input_bass_pulse_impact = models.TextField(null=True)
    input_bass_story_speed = models.TextField(null=True)
    input_end_second = models.TextField(null=True)
    input_mids_pulse_impact = models.TextField(null=True)
    input_mids_story_speed = models.TextField(null=True)
    input_smoothing = models.TextField(null=True)
    input_start_second = models.TextField(null=True)
    input_story = models.TextField(null=True)
    input_style_suffix = models.TextField(null=True)
    input_text_prompt_bass = models.TextField(null=True)
    input_text_prompt_mids = models.TextField(null=True)
    input_text_prompt_treble = models.TextField(null=True)
    input_trebles_pulse_impact = models.TextField(null=True)
    input_trebles_story_speed = models.TextField(null=True)
    input_file_image = models.TextField(null=True)
    input_frame_rate = models.TextField(null=True)
    input_imagemodel = models.TextField(null=True)
    input_image_model = models.TextField(null=True)
    input_colorize = models.TextField(null=True)
    input_city = models.TextField(null=True)
    input_country = models.TextField(null=True)
    input_doctolib_email = models.TextField(null=True)
    input_doctolib_password = models.TextField(null=True)
    input_dose = models.TextField(null=True)
    input_start_date = models.TextField(null=True)
    input_twofa_code = models.TextField(null=True)
    input_vaccine = models.TextField(null=True)
    input_prompts = models.TextField(null=True)

    def output_video_tag(self):
        return mark_safe('<video src="https://pollinations.ai/ipfs/{}/output/video.mp4" width="150" height="150" autoplay=true />'.format(self.cid))

def empty_jsonb_array():
    return []


class Task(models.Model):
    cid = models.CharField(max_length=255, unique=True)
    state_updates = models.JSONField(default=empty_jsonb_array)

    def add_state_update(self, log: str):
        self.state_updates.append({"timestamp": datetime.datetime.now().timestamp(), "log": log})
        self.save()
