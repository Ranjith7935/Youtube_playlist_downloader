import os
from yt_dlp import YoutubeDL

def download_playlist(playlist_url, download_path="downloads"):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Set up options for yt-dlp
    options = {
        'format': 'best',  # Download the best quality video available
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Path template to save the videos
        'noplaylist': False,  # Keep playlist downloading enabled
        'retries': 3,  # Number of retries in case of download failure
        'continue': True,  # Continue partial downloads
        'quiet': False,  # Display logs and progress
    }

    try:
        with YoutubeDL(options) as ydl:
            # Download the entire playlist
            ydl.download([playlist_url])
        print(f"Playlist downloaded successfully at: {download_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")  # Prompt the user for playlist URL
    download_playlist(playlist_url)

