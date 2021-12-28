import pathlib
import shutil
import subprocess
import os.path

ipfs_temp_folder = os.environ.get("IPFS_TEMP_FOLDER") or "tmp"
pathlib.Path(ipfs_temp_folder).mkdir(parents=True, exist_ok=True)


def cid_to_gateway_url(cid: str, folder=""):
    return f"https://ipfs.pollinations.ai/ipfs/{cid}/{folder}"


def delete_downloaded_cid(cid: str):
    if os.path.isfile(get_local_folder_for_cid(cid)):
        os.remove(get_local_folder_for_cid(cid))
    else:
        shutil.rmtree(get_local_folder_for_cid(cid), ignore_errors=True)


def get_local_folder_for_cid(cid: str):
    return f"{ipfs_temp_folder}/{cid}"


def download_cid(cid):
    """
    Downloads the file with the given CID.
    """
    ipfs_process = subprocess.Popen(
        [
            "/app/go-ipfs/ipfs",
            "--api",
            "/ip4/65.108.44.19/tcp/5005",
            "get",
            "-o",
            get_local_folder_for_cid(cid),
            cid,
        ]
    )
    return ipfs_process.wait()


class DownloadedCID:
    def __init__(self, cid):
        self.cid = cid
        self.local_folder = get_local_folder_for_cid(cid)

    def __enter__(self):
        download_cid(self.cid)
        return self.local_folder

    def __exit__(self, exc_type, exc_val, exc_tb):
        delete_downloaded_cid(self.cid)
