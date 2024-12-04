from youtube_transcript_api import YouTubeTranscriptApi
import os

def extract_transcript_from_youtube(video_url, filename):
    video_id = video_url.split('=')[-1]
    #filename = f"../data/transcripts/transcript_{video_id}.txt"
    filename = f"transcript_{video_id}.txt"
    extracted_transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    transcript = ""
    for script in extracted_transcript:
        transcript += script['text'] + "\n"
    with open(filename, "w") as f:
        f.write(transcript)
    f.close()

video_url = "https://www.youtube.com/watch?v=OEdJamFQDZo"
extract_transcript_from_youtube(video_url)
