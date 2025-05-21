import argparse
from downloader import start_download

def main():
    parser = argparse.ArgumentParser(description="YouTube Downloader")
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="Download only the audio as MP3"
    )
    args = parser.parse_args()

    start_download(audio_only=args.audio_only)

if __name__ == "__main__":
    main()
