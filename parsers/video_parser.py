from pytubefix import YouTube
import logging
import cv2
import os

logging.basicConfig(level=logging.DEBUG)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    logging.debug(f'Download progress: {percentage_of_completion:.2f}%')

def download_video(url, output_path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            logging.debug(f"Starting download of {url}")
            stream.download(output_path)
            logging.debug(f"Finished download of {url}")
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
