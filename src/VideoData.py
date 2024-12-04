from audio_extractor import extract_audio_from_youtube
from screenshot_extractor import extract_screenshots_from_youtube
from transcript_extractor import extract_transcript_from_youtube
# use pil for image processing
class VideoData:
    def __init__(self, url):
        self.url = url
    
    def extract_data_from_youtube(video_url):
        # get filenames for respective functions
        audio_filename = "../data/audios"
        video_filename = "../data/videos"
        transcript_filename = "../data/transcripts"
        
        # extract audio
        extract_audio_from_youtube(video_url, audio_filename)
        
        # extract screenshots
        extract_screenshots_from_youtube(video_url, video_filename)
        
        # extract transcripts
        extract_transcript_from_youtube(video_url, transcript_filename)
        
        