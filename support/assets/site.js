// The optional tutorial appears automatically once basic-guide.mp4 is added.
// No video is downloaded until the user presses Play (preload="none").
const videoGuide = document.getElementById('video-guide');

if (videoGuide) {
  fetch('./assets/videos/basic-guide.mp4', { method: 'HEAD' })
    .then((response) => {
      if (response.ok) {
        videoGuide.hidden = false;
      }
    })
    .catch(() => {
      // Screenshots and written instructions remain available without a video.
    });
}
