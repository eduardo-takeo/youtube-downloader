import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "data", "input", "links.txt")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "data", "output", "downloads")
ERROR_FILE = os.path.join(BASE_DIR, "logs", "errors.txt")
