import time
from scraper import VideoDownloader

with open('urls.txt', 'r') as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()
    if not url:
        continue
    print(f'開始下載: {url}')
    downloader = VideoDownloader(url)
    time.sleep(30)