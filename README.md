# atelier-synth

Static single-file web apps, deployed on Vercel.

| Path | Project |
| --- | --- |
| `/` (`index.html`) | Atelier — synth workstation |
| `/rehome/` (`rehome/index.html`) | ReHome — visualise a renovation design and get a cost attached to it |

## ReHome: offline and locked down

ReHome currently runs fully offline: open `rehome/index.html` straight from disk and it works with no network.

- Fonts (Cormorant Garamond, DM Sans; SIL OFL, licences in `rehome/fonts/`) are embedded in the page.
- All imagery is drawn in the page as SVG illustrations. There are no remote images.
- Uploaded photos are read in the browser only and never sent anywhere. Only JPG/PNG/WEBP/GIF up to 15 MB are accepted.
- A Content-Security-Policy (in the page and in `vercel.json`) blocks every network request: no scripts, styles, images, fonts or fetches from anywhere else.
- The Pinterest import (it sent your access token through a third-party proxy) and the paste-an-image-URL fields have been removed.
