Here is the complete `README.md` content you can copy and paste:

```markdown
# YouTube Parser

This project allows you to download any YouTube video or playlist, extract images and text from the video, and generate a PDF or DOC file containing the images and associated text.

## Features
- Download a single YouTube video or an entire playlist.
- Extract images from the video frames.
- Extract and associate text with images.
- Generate a PDF or DOC file with the extracted content.

## Installation

First, clone the repository:
```bash
git clone https://github.com/AlterEgo00001/YouTube_parser.git
cd YouTube_parser
```

Install the required Python libraries:
```bash
pip install pytube opencv-python pytesseract python-docx reportlab
```

## Usage

To use the YouTube parser, run the following command:
```bash
python main.py <YouTube URL> --output <pdf|docx>
```

### Example
Download a YouTube video and generate a PDF:
```bash
python main.py https://www.youtube.com/watch?v=example_video_id --output pdf
```

Download a YouTube playlist and generate a DOCX:
```bash
python main.py https://www.youtube.com/playlist?list=example_playlist_id --output docx
```

## Project Structure
```
YouTube_parser/
├── main.py
├── parsers/
│   ├── video_parser.py
│   ├── image_text_extractor.py
│   ├── document_generator.py
├── outputs/
│   ├── documents/
│   ├── images/
└── utils/
    ├── menu.py
```

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
```

You can now copy this content into your `README.md` file.
