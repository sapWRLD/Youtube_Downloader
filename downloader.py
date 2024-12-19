from pytube import YouTube, Playlist, Channel
import os

# Get the desktop path dynamically
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

def playlist(url):
    try:
        playlist = Playlist(url)
        print(f'Number of videos in playlist: {len(playlist.video_urls)}')
        for video in playlist.videos:
            try:
                stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                if stream:
                    stream.download(output_path=desktop)
                    print(f'Video downloaded: {video.title}')
                else:
                    print(f'No suitable stream found for video: {video.title}')
            except Exception as e:
                print(f'Error downloading video {video.title}: {e}')
    except Exception as e:
        print(f'Error processing playlist: {e}')

def video(url):
    try:
        yt = YouTube(url)
        print(f'Video title: {yt.title}')
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            stream.download(output_path=desktop)
            print(f'Video downloaded: {yt.title}')
        else:
            print('No suitable stream found.')
    except Exception as e:
        print(f'Error downloading video: {e}')

def channel(url):
    try:
        channel = Channel(url)
        print(f'Downloading videos from channel: {channel.channel_name}')
        for video in channel.videos:
            try:
                stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                if stream:
                    stream.download(output_path=desktop)
                    print(f'Video downloaded: {video.title}')
                else:
                    print(f'No suitable stream found for video: {video.title}')
            except Exception as e:
                print(f'Error downloading video {video.title}: {e}')
    except Exception as e:
        print(f'Error processing channel: {e}')

def main():
    try:
        pick = input("Enter 1 for playlist, 2 for video, 3 for channel\n")
        if pick == "1":
            url = input("Enter the URL of the playlist: ")
            playlist(url)
        elif pick == "2":
            url = input("Enter the URL of the video: ")
            video(url)
        elif pick == "3":
            url = input("Enter the URL of the channel: ")
            channel(url)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
