from pathlib import Path
from typing import Literal, Optional

from huggingface_hub import HfApi, HfFolder, hf_hub_download, snapshot_download
from loguru import logger


RepoType = Literal["dataset", "model"]


def connect_to_api() -> HfApi:
    """Connect to the HF API, making sure that things work."""
    api = HfApi()

    token = HfFolder.get_token()
    if token is None:
        raise OSError(
            "You need to provide a `token` or be logged in to Hugging Face with `huggingface-cli login`."
        )

    return api


def upload_file(*, path: Path, path_in_repo: str, hf_repo_id: str, repo_type: RepoType) -> None:
    """Upload a file to the HF repo.

    Args:
        path: Path to the file to upload.
        path_in_repo: Path to the file in the repo, relative to the root.
        hf_repo_id: ID of the repo to upload to.
        repo_type: Type of the repo to upload to.
    """
    assert path.exists(), f"File {path} does not exist."
    assert path.is_file(), f"Path {path} is not a file."

    api = connect_to_api()

    # Create the repo if it doesnt already exist
    api.create_repo(hf_repo_id, repo_type=repo_type, exist_ok=True)

    # Upload the file
    logger.debug(f"Uploading {path} to {hf_repo_id}...")
    api.upload_file(
        path_or_fileobj=path,
        path_in_repo=path_in_repo,
        repo_id=hf_repo_id,
        repo_type=repo_type,
        commit_message=f"Upload {path} to {path_in_repo}",
    )
    logger.debug(f"Uploaded {path} to {hf_repo_id}.")


def upload_folder(*, path: Path, path_in_repo: str, hf_repo_id: str, repo_type: RepoType) -> None:
    """Upload a folder to the HF repo."""
    assert path.exists(), f"Folder {path} does not exist."
    assert path.is_dir(), f"Path {path} is not a directory."

    api = connect_to_api()
    api.create_repo(hf_repo_id, repo_type=repo_type, exist_ok=True)

    logger.debug("Starting the upload...")
    api.upload_folder(
        folder_path=path,
        repo_id=hf_repo_id,
        repo_type=repo_type,
        path_in_repo=path_in_repo,
        commit_message=f"Upload {path}",
    )
    logger.debug(f"Finished uploading {path} to the hub.")


def download_file(
    *,
    repo_id: str,
    repo_type: RepoType,
    filename: str,
    subfolder: Optional[str] = None,
    force_download: bool = False,
) -> Path:
    """Download a file from the HF repo.

    If the file has already been downloaded, it will return the cached version by default.
    """
    logger.debug(f"Downloading {filename} from {repo_id}...")
    path = Path(
        hf_hub_download(
            repo_id,
            filename,
            subfolder=subfolder,
            repo_type=repo_type,
            force_download=force_download,
            resume_download=True,
        )
    )
    logger.debug(f"Downloaded {filename} -> {path} from {repo_id}.")
    return path


def download_folder(
    *,
    repo_id: str,
    folder_name: str,
    repo_type: RepoType,
    max_workers: int = 1,
    force_download: bool = False,
) -> Path:
    """Download a folder from the HF repo.

    The provided folder name should be the path to the folder from the root of the repo, since we
    use the pattern to get it.
    """
    logger.debug(f"Downloading {folder_name} from {repo_id}...")
    path = Path(
        snapshot_download(
            repo_id=repo_id,
            allow_patterns=f"{folder_name}/**",
            repo_type=repo_type,
            max_workers=max_workers,
            resume_download=True,
            force_download=force_download,
        )
    )
    logger.debug(f"Downloaded {folder_name} -> {path} from {repo_id}.")
    return path
