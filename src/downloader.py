import os
import yt_dlp
from config import INPUT_FILE, OUTPUT_FOLDER, ERROR_FILE
from utils import is_valid_youtube_url


def get_ydl_opts(output_folder):
    outtmpl = f"{output_folder}/%(title)s.%(ext)s"

    return {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "outtmpl": outtmpl,
        "nocheckcertificate": True,
        "ignoreerrors": True,
        "no_warnings": True,
        "quiet": False,
        "extract_flat": False,
        "noplaylist": True,
        "retries": 3,
        "abort_on_unavailable_fragments": True,
        "no-keep-fragments": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0",
        },
    }


def start_download():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    if os.path.exists(ERROR_FILE):
        os.remove(ERROR_FILE)

    if not os.path.exists(INPUT_FILE):
        print(f"Input file not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r") as file:
        video_urls = [
            line.strip()
            for line in file
            if line.strip() and is_valid_youtube_url(line.strip())
        ]

    if not video_urls:
        print("No valid YouTube URLs found.")
        return

    for url in video_urls:
        download_audio(url)

    if os.path.exists(ERROR_FILE) and os.path.getsize(ERROR_FILE) > 0:
        print(f"\nSome downloads failed. See: {ERROR_FILE}")

    print("\nAll downloads finished!")


def download_audio(video_url):
    try:
        ydl_opts = get_ydl_opts(OUTPUT_FOLDER)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)
            video_name = ydl.prepare_filename(video_info)
            filename = os.path.splitext(video_name)[0] + ".mp3"

            if os.path.exists(filename):
                print(f"File already exists, skipping: {filename}")
                return

            ydl.download([video_url])
            print(f"Download completed: {video_url}")
    except Exception as e:
        with open(ERROR_FILE, "a", encoding="utf-8") as f:
            f.write(f"{video_url} - Error: {str(e)}\n")
        print(f"Error processing {video_url}: {e}")
