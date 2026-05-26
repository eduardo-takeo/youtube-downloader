from downloader import start_download
from updater import check_and_update


def main():
    check_and_update()
    start_download()


if __name__ == "__main__":
    main()
