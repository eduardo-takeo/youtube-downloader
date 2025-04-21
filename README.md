# youtube-downloader

Simple script to download music directly from YouTube

## 🛠️ Prerequisites

- [python3](https://www.python.org/downloads/) installed
- [ffmpeg](https://www.ffmpeg.org/download.html) installed

  - macos:

  ```bash
  brew install ffmpeg
  ```

  - linux:

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

  - windows:
    1. Download installer: [FFmpeg Builds](https://www.ffmpeg.org/download.html).
    2. Extract .zip file.
    3. Add binary to PATH variable.

## 🧰 Usage

1. Activate virtual env

```bash
source env/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Put YouTube video links inside **links.txt** file

```
# 🚧 INSERT ONE LINK PER LINE

https://www.youtube.com/watch?v=<VIDEO_ID>
https://www.youtube.com/watch?v=<VIDEO_ID>
https://www.youtube.com/watch?v=<VIDEO_ID>
```

4. Run script

**Download video**

```bash
python -m src.youtube_downloader
```

**Download audio only**

```bash
python -m src.youtube_downloader --audio-only
```
