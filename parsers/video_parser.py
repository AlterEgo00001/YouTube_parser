import logging
import os
import cv2
import yt_dlp

logging.basicConfig(level=logging.DEBUG)

def download_video(url, output_path):
    """Скачивает видео с YouTube, используя yt-dlp"""
    try:
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'progress_hooks': [on_progress]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logging.debug(f"Downloading video from {url}")
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            file_name = os.path.join(output_path, f"{video_title}.mp4")
            if os.path.exists(file_name):
                logging.debug(f"Download complete: {file_name}")
                return file_name
            else:
                logging.error("Download failed or file was not created.")
                return None
    except Exception as e:
        logging.error(f"Error downloading video: {e}")
        return None

def on_progress(d):
    if d['status'] == 'downloading':
        p = d['_percent_str'].strip()
        logging.debug(f"Download progress: {p}")

def extract_frames(video_path):
    """Извлекает кадры из видеофайла"""
    try:
        cap = cv2.VideoCapture(video_path)
        frames = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()
        logging.debug(f"Extracted {len(frames)} frames from {video_path}")
        return frames
    except Exception as e:
        logging.error(f"Error extracting frames from {video_path}: {e}")
        return []
