function parseVideo() {
  const url = document.getElementById('url').value;
  const format = document.getElementById('format').value;
  const status = document.getElementById('status');
  
  status.textContent = 'Loading video...';
  const video = document.createElement('video');
  video.crossOrigin = "anonymous";
  video.src = url;
  video.load();
  
  video.addEventListener('loadeddata', () => {
    status.textContent = 'Video loaded. Extracting frames...';
    extractFrames(video, format);
  });
  
  video.addEventListener('error', (e) => {
    console.error('Error loading video:', e);
    status.textContent = 'Error loading video';
  });
}

function extractFrames(video, format) {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  
  const frames = [];
  const interval = 1;
  let currentTime = 0;

  function captureFrame() {
    video.currentTime = currentTime;
    video.addEventListener('seeked', function onSeeked() {
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      frames.push(canvas.toDataURL('image/jpeg'));
      currentTime += interval;
      if (currentTime < video.duration) {
        captureFrame();
      } else {
        video.removeEventListener('seeked', onSeeked);
        processFrames(frames, format);
      }
    }, { once: true });
  }

  captureFrame();
}

function processFrames(frames, format) {
  const status = document.getElementById('status');
  status.textContent = 'Processing frames...';
  
  let content = 'Extracted frames:\n\n';
  frames.forEach((frame, index) => {
    content += `Frame ${index + 1}: ${frame}\n`;
  });

  downloadFile(content, format === 'pdf' ? 'output.pdf' : 'output.docx');
  status.textContent = 'Download ready';
}

function downloadFile(content, filename) {
  const blob = new Blob([content], { type: 'text/plain' });
  const link = document.createElement('a');
  link.href = window.URL.createObjectURL(blob);
  link.download = filename;
  link.click();
}
