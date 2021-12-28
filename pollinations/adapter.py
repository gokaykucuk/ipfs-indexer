import glob
import os
import re

import pandas as pd

from pollinations.models import Content, Task
from repositories.ipfs import get_local_folder_for_cid, download_cid, delete_downloaded_cid, DownloadedCID


def is_cid_eligible(cid: str):
    return os.path.exists(get_local_folder_for_cid(cid) + "/output/done")


def extract_cid_meta(cid):
    local_folder_for_cid = get_local_folder_for_cid(cid)
    files_and_folders_for_cid = glob.glob(local_folder_for_cid + "/**", recursive=True)
    files_and_folders_df = pd.Series(files_and_folders_for_cid)
    files_and_folders_df = files_and_folders_df.str.replace(local_folder_for_cid, "")
    files_and_folders_df = files_and_folders_df[~files_and_folders_df.str.contains("\.")]

    readable_files_list = files_and_folders_df.tolist()

    readable_files_list.remove("/")
    readable_files_list.remove("/input")
    readable_files_list.remove("/output")

    # Clear continuation for now
    regex = re.compile(r'.*continuation.*')
    filtered_files_list = [i for i in readable_files_list if not regex.search(i)]

    cid_props = {"cid": cid}
    for file_name in filtered_files_list:
        with open(local_folder_for_cid + file_name) as f:
            prop_key = file_name.replace("/", "_")[1:]
            cid_props[prop_key] = f.read()
        with open(local_folder_for_cid + "/input/notebook.ipynb") as f:
            cid_props["input_notebook_ipynb"] = f.read()
    return cid_props


def process_cid(task: Task):
    with DownloadedCID(task.cid) as d:
        if is_cid_eligible(task.cid):
            task.add_state_update("started_downloading")
            cid_metadata = extract_cid_meta(task.cid)
            task.add_state_update("finished_downloading")
            content_in_db = Content.objects.get_or_create(cid=task.cid, defaults=cid_metadata)
            task.add_state_update("content_saved_to_db")
            return content_in_db[0]
        else:
            task.add_state_update("error_cid_not_eligible")
