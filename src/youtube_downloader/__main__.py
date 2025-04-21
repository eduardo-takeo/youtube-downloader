from . import app
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Downloader")
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="Download only audio in MP3 format.",
    )
    args = parser.parse_args()

    app.start_download(audio_only=args.audio_only)
