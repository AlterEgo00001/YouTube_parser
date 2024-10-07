from pytube import YouTube
import logging
import cv2
import os

logging.basicConfig(level=logging.DEBUG)

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            stream.download(output_path)
            return os.path.join(output_path, stream.default_filename)
        else:
            logging.error("No suitable streams found.")
            raise Exception("No suitable streams found.")
    except Exception as e:
        logging.error(f"Error downloading video: {e}")
        raise

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames
