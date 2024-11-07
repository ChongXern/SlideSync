import yt_dlp
import os

def extract_audio_from_youtube(video_url, filename):
    video_id = video_url.split('=')[-1]

    audio_filename = f"audio_{video_id}.mp3"
    output_path = os.path.join(filename, audio_filename)
    os.makedirs(filename, exist_ok=True)
    ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            'quiet': True
            }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print(f"audio saved to {output_path}")
    return output_path

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
filename = "../data/audio"
#os.makedirs(filename, exist_ok=True)
extract_audio_from_youtube(video_url, filename)
