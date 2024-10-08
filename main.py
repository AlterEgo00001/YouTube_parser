import argparse
import os
from parsers.video_parser import download_video, extract_frames
from parsers.image_text_extractor import associate_text_with_images
from parsers.document_generator import generate_docx, generate_pdf
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Parser")
    parser.add_argument('url', type=str, help='URL of the YouTube video or playlist')
    parser.add_argument('--output', type=str, choices=['pdf', 'docx'], default='pdf', help='Output file format')
    args = parser.parse_args()

    # Определяем, является ли это плейлистом или одиночным видео
    if 'playlist' in args.url:
        from pytubefix import Playlist  # импортируем локально, если это действительно плейлист
        pl = Playlist(args.url)
        for video_url in pl.video_urls:
            logging.debug(f"Processing video URL: {video_url}")
            process_video(video_url, args.output)
    else:
        process_video(args.url, args.output)

def process_video(url, output_format):
    video_path = download_video(url, 'outputs/videos')
    if not video_path:
        logging.error(f"Failed to download video from {url}")
        return

    frames = extract_frames(video_path)
    if not frames:
        logging.error(f"Failed to extract frames from {video_path}")
        return

    text_image_pairs = associate_text_with_images(frames)

    if output_format == 'pdf':
        generate_pdf(text_image_pairs, 'outputs/documents/output.pdf')
    else:
        generate_docx(text_image_pairs, 'outputs/documents/output.docx')

if __name__ == '__main__':
    main()
