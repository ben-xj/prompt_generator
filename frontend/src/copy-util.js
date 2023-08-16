// copy-util.js

export function copyToClipboard(text) {

  // Use navigator clipboard api if supported
  if (navigator.clipboard) {
    return navigator.clipboard.writeText(text);
  }

  // Else use older execCommand method
  else {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try {
      document.execCommand('copy');
    } catch (err) {
      console.error('Unable to copy', err);
    }

    document.body.removeChild(textArea);
  }

}