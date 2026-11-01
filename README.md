# The Odyssey in Art

A "film" of the Odyssey made from about a thousand public-domain works of art from Wikimedia Commons, in chronological scene order.

- `index.html` — the viewer. **Film** mode shows each image for 3 frames. **Click-through** mode shows the title, artist and description, and has a collapsible scene sidebar. Both modes come in **Complete** and **Concise** versions and have a Story switch for side stories without Odysseus.
- `odyssey.json` — scenes and images. `src` links to the original file and `display` is Commons' 1280 px rendering.

Serve the folder over HTTP so the page can load the JSON, for example with `python3 -m http.server 8000`, then open http://localhost:8000. Opened as a local file, the page asks you to pick `odyssey.json` instead.
