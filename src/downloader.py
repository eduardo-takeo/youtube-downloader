import os
import yt_dlp
from config import INPUT_FILE,OUTPUT_FOLDER, ERROR_FILE
from utils import is_valid_youtube_url

def get_ydl_opts(output_folder, audio_only):
    outtmpl = f'{output_folder}/%(title)s.%(ext)s'
    
    if audio_only:
        postprocessors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        format_selector = 'bestaudio/best'
    else:
        postprocessors = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
        
        format_selector = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best[ext=mp4]/best'
    
    return {
        'format': format_selector,
        'postprocessors': postprocessors,
        'outtmpl': outtmpl,
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'no_warnings': True,
        'quiet': False,
        'extract_flat': False,
        'noplaylist': True,
        'retries': 3,
        'fragment_retries': 3,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0',
        }
    }

def start_download(audio_only=False):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    if os.path.exists(ERROR_FILE):
        os.remove(ERROR_FILE)

    if not os.path.exists(INPUT_FILE):
        print(f"Input file not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r") as file:
        video_urls = [line.strip() for line in file if line.strip() and is_valid_youtube_url(line.strip())]

    if not video_urls:
        print("No valid YouTube URLs found.")
        return

    for url in video_urls:
        download_audio(url, audio_only)

    if os.path.exists(ERROR_FILE) and os.path.getsize(ERROR_FILE) > 0:
        print(f"\nSome downloads failed. See: {ERROR_FILE}")

    print("\nAll downloads finished!")

def download_audio(video_url, audio_only):
    try:
        ydl_opts = get_ydl_opts(OUTPUT_FOLDER, audio_only)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            filename = ydl.prepare_filename(info_dict)
            
            if audio_only:
                filename = os.path.splitext(filename)[0] + ".mp3"
            else:
                filename = os.path.splitext(filename)[0] + ".mp4"

            if os.path.exists(filename):
                print(f"File already exists, skipping: {filename}")
                return

            ydl.download([video_url])
            print(f"Download completed: {video_url}")
    except Exception as e:
        with open(ERROR_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{video_url} - Error: {str(e)}\n")
        print(f"Error processing {video_url}: {e}")
