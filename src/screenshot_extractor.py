import os
import cv2
import yt_dlp

def download_video(url, save_path):
    video_id = url.split('=')[-1]
    filename = f"video_{video_id}.mp4"
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(save_path, filename)
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return os.path.join(save_path, filename), video_id

def capture_screenshots(video_path, save_folder, video_id, interval=10):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_rate = int(fps * interval)
    frame_count = 0
    screenshot_count = 1

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame_count += 1

        if frame_count % frame_rate == 0:
            screenshot_filename = f"screenshot_{video_id}_{screenshot_count}.png"
            screenshot_path = os.path.join(save_folder, screenshot_filename)
            cv2.imwrite(screenshot_path, frame)
            print(f"Screenshot {screenshot_count} saved at {screenshot_path}")
            screenshot_count += 1

    video.release()
    
def extract_screenshots_from_youtube(video_url, save_folder):
    video_id = video_url.split('=')[-1]
    video_path, video_id = download_video(video_url, save_folder)
    capture_screenshots(video_path, save_folder, video_id)
    os.remove(video_path)
    
'''
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    save_folder = "videos"
    print("Downloading video...")
    video_path, video_id = download_video(video_url, save_folder)

    print("Capturing screenshots...")
    capture_screenshots(video_path, save_folder, video_id)
    print("Finished capturing screenshots.")
    '''