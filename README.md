# youtube-downloader

Simple script to download music directly from YouTube

**🚨 IMPORTANT 🚨**

YouTube make changes on the way it serves it's videos, make sure **yt-dlp** library is always up to date:

`pip install -U yt-dlp`

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

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Put YouTube video links inside **links.txt** file

```
# 🚧 INSERT ONE LINK PER LINE

https://www.youtube.com/watch?v=<VIDEO_ID>
https://www.youtube.com/watch?v=<VIDEO_ID>
https://www.youtube.com/watch?v=<VIDEO_ID>
```

3. Run script

**Download video**

```bash
./run.sh
```

**Download audio only**

```bash
./run.sh --audio-only
```
