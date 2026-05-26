import json
import os
import subprocess
import sys

import yt_dlp


def check_and_update() -> None:
    current = yt_dlp.version.__version__

    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"yt-dlp {current} (could not check for updates)")
        return

    outdated = json.loads(result.stdout)
    pkg = next((p for p in outdated if p["name"] == "yt-dlp"), None)

    if pkg is None:
        print(f"yt-dlp {current} is already the latest version.")
        return

    latest = pkg["latest_version"]
    print(f"A new version of yt-dlp is available: {latest} (current: {current})")
    answer = input("Update to the latest version? (y/N): ").strip().lower()

    if answer != "y":
        return

    print("Updating yt-dlp...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print("yt-dlp updated successfully!")
        print("Restarting to load the new version...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        print(f"Update failed:\n{result.stderr}")
