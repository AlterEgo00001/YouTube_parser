function parseVideo() {
  const url = document.getElementById('url').value;
  const format = document.getElementById('format').value;

  // Local implementation to handle video parsing
  // This will require Python script execution on the client machine
  
  fetch(`http://localhost:5000/parse`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `url=${encodeURIComponent(url)}&format=${encodeURIComponent(format)}`
  })
  .then(response => response.blob())
  .then(blob => {
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = format === 'pdf' ? 'output.pdf' : 'output.docx';
    link.click();
  })
  .catch(error => console.error('Error:', error));
}
