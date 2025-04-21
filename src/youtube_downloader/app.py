import os
import yt_dlp

def download_audio(video_url, output_folder, error_file):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'nocheckcertificate': True,
            'ignoreerrors': True,
            'no_warnings': True,
            'quiet': False,
            'extract_flat': False,
            'noplaylist': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            }
        }
        # Check if the URL is valid before trying to download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.extract_info(video_url, download=False)
                ydl.download([video_url])
                print(f"Download concluído: {video_url}")
            except Exception as e:
                with open(error_file, 'a', encoding='utf-8') as f:
                    f.write(f"{video_url} - Error: {str(e)}\n")
                print(f"Error processing video {video_url}: {e}")
                
    except Exception as e:
        with open(error_file, 'a', encoding='utf-8') as f:
            f.write(f"{video_url} - Erro: {str(e)}\n")
        print(f"Erro ao processar o vídeo {video_url}: {e}")


def start_download():
    # File containing the links
    input_file = "data/input/links.txt"
    # Output folder
    output_folder = "data/output/downloads"
    error_file = "output/errors.txt"
    os.makedirs(output_folder, exist_ok=True)
    
    # Clear the error file if it exists
    if os.path.exists(error_file):
        os.remove(error_file)

    # Check if the file exists
    if not os.path.exists(input_file):
        print(
            f"File {input_file} not found. Ensure it exists.")
        return

    # Read the links from the file
    with open(input_file, "r") as file:
        video_urls = [line.strip() for line in file if line.strip()]

    if not video_urls:
        print(
            f"The file {input_file} is empty. Add YouTube links (one per line).")
        return

    # Process each URL
    for url in video_urls:
        download_audio(url, output_folder, error_file)

    if os.path.exists(error_file) and os.path.getsize(error_file) > 0:
        print(f"\nSome videos could not be downloaded. Check {error_file} for more details.")
    
    print("\nAll downloads completed!")