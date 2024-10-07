import argparse
from parsers.video_parser import download_video, extract_frames
from parsers.image_text_extractor import associate_text_with_images
from parsers.document_generator import generate_docx, generate_pdf

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Parser")
    parser.add_argument('url', type=str, help='URL of the YouTube video or playlist')
    parser.add_argument('--output', type=str, choices=['pdf', 'docx'], default='pdf', help='Output file format')
    args = parser.parse_args()

    video_path = download_video(args.url, 'outputs/videos')
    frames = extract_frames(video_path)
    text_image_pairs = associate_text_with_images(frames)

    if args.output == 'pdf':
        generate_pdf(text_image_pairs, 'outputs/documents/output.pdf')
    else:
        generate_docx(text_image_pairs, 'outputs/documents/output.docx')

if __name__ == '__main__':
    main()
