import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import subprocess

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def download_file(url, destination):
    response = requests.get(url, headers=headers, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024

    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(destination, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

def run_command(command):
    try:
        # Blender komutunu subprocess ile başlat
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Çıktıyı okuyarak anlık olarak ekrana yazdır
        for line in process.stdout:
            print(line, end='')

        # Hata durumunda stderr'u yazdır
        for line in process.stderr:
            print(f"Hata: {line}", end='')

        # Sürecin tamamlanmasını bekle
        process.wait()
    except Exception as e:
        print(f"Hata: {e}")

def get_latest_blender_version_url():
    print("Getting latest Blender version..")
    url = "https://mirror.freedif.org/blender/release/"
    release_res = requests.get(url, headers=headers)
    release_soup = BeautifulSoup(release_res.text, "html.parser")
    a_tag_release_list = release_soup.find_all("a")
    blender_url = a_tag_release_list[5]["href"]
    url += blender_url
    blender_res = requests.get(url, headers=headers)
    blender_soup = BeautifulSoup(blender_res.text, "html.parser")
    blender_body_tag = blender_soup.body
    for string in blender_body_tag.strings:
        if "tar.xz" in string:
            blender_version_linux_url = string
    url += blender_version_linux_url
    return url

