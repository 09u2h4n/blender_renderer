from .utils import download_file, get_latest_blender_version_url
import tarfile
import os
import stat

def download_blender(blender_version="4.0.2", download_path="default", redownload=False):
    blender_urls = {
        "3.6.4": "https://ftp.nluug.nl/pub/graphics/blender/release/Blender3.6/blender-3.6.4-linux-x64.tar.xz",
        "4.0.2": "https://ftp.nluug.nl/pub/graphics/blender/release/Blender4.0/blender-4.0.2-linux-x64.tar.xz",
        "latest": get_latest_blender_version_url()
    }

    blender_url = blender_urls.get(blender_version)

    if download_path == "default":
        download_path = os.path.join("content", "blender_downloads")

    if not blender_url:
        print(f"Blender version {blender_version} is not available for download.")
        return

    blender_tar_file_name = os.path.basename(blender_url)
    destination = os.path.join(download_path, blender_tar_file_name)

    if not redownload:
      # Check if Blender is already downloaded
      if os.path.exists(destination):
          print(f"Blender {blender_version} is already downloaded.")
          return
      else:
          os.makedirs(download_path, exist_ok=True)

    print(f"Downloading Blender {blender_version}")

    download_file(blender_url, destination)

    print("\n")
    print(f"Blender {blender_version} has been downloaded to {destination}")

def set_blender_for_linux(blender_version="4.0.2", use_blender_on_drive=False, download_path="default"):
    blender_download_path = download_path

    if download_path == "default":
        download_path = os.path.join("content", "blender_downloads")

    if use_blender_on_drive:
        try:
            from google.colab import drive
        except:
            print("Environment is not google colab!")
        drive.mount("/content/g_drive")
        blender_drive_dir = "/content/g_drive/MyDrive/blender_downloads"
        blender_extract_path = blender_drive_dir
    else:
        blender_extract_path = blender_download_path

    blender_folder_name = f"blender-{blender_ver}-linux-x64"
    blender_tar_file_name = blender_folder_name + ".tar.xz"
    blender_archive_path = os.path.join(blender_download_path, blender_tar_file_name)

    # Check if Blender archive is already extracted
    if not os.path.exists(os.path.join(blender_extract_path, blender_folder_name)):
        if not os.path.exists(blender_archive_path):
            print(f"Blender archive not found at {blender_archive_path}.")
            return

        # Extract the Blender archive
        with tarfile.open(blender_archive_path, 'r:xz') as tar:
            tar.extractall(path=blender_extract_path)

        print(f"Blender {blender_ver} has been extracted to {blender_extract_path}.")

    # Set Blender executable path
    blender_path = os.path.join(blender_extract_path, blender_folder_name, "blender")
    if os.path.exists(blender_path):
        os.environ["BLENDER_PATH"] = blender_path

        # Ensure executable permissions
        os.chmod(blender_path, stat.S_IRWXU)

        print(f"Blender {blender_ver} has been set successfully.")
    else:
        print(f"Blender executable not found at {blender_path}.")

    # Remove the downloaded Blender archive
    try:
        os.remove(blender_archive_path)
    except FileNotFoundError:
        pass

