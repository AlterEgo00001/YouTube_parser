function parseVideo() {
  const url = document.getElementById('url').value;
  const format = document.getElementById('format').value;
  const status = document.getElementById('status');
  const videoId = getYouTubeVideoId(url);

  if (!videoId) {
    alert('Invalid YouTube URL');
    return;
  }

  status.textContent = 'Fetching video details...';

  fetch(`https://www.googleapis.com/youtube/v3/videos?id=${videoId}&key=YOUR_API_KEY&part=snippet,contentDetails`)
    .then(response => response.json())
    .then(data => {
      if (data.items.length === 0) {
        alert('Video not found');
        status.textContent = 'Video not found';
        return;
      }

      status.textContent = 'Processing video data...';

      const videoData = data.items[0];
      const videoTitle = videoData.snippet.title;
      const videoDescription = videoData.snippet.description;

      const output = `Title: ${videoTitle}\n\nDescription: ${videoDescription}\n\nFormat: ${format}`;
      downloadFile(output, format === 'pdf' ? 'output.pdf' : 'output.docx');

      status.textContent = 'Download ready';
    })
    .catch(error => {
      console.error('Error:', error);
      status.textContent = 'Error occurred: ' + error.message;
    });
}

function getYouTubeVideoId(url) {
  const match = url.match(/(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)/);
  return match ? match[1] : null;
}

function downloadFile(content, filename) {
  const blob = new Blob([content], { type: 'text/plain' });
  const link = document.createElement('a');
  link.href = window.URL.createObjectURL(blob);
  link.download = filename;
  link.click();
}
