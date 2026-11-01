# The Odyssey in Art

A "film" of the Odyssey made from about a thousand public-domain works of art from Wikimedia Commons, in chronological scene order.

- `index.html` — the viewer. **Film** mode shows each image for 3 frames, centred on Odysseus' head where one is marked. **Click-through** mode shows the title, artist and description, and has a collapsible scene sidebar. Clicking Odysseus' head marks it for the film. Both modes come in **Complete** and **Concise** versions and have a Story switch for side stories without Odysseus.
- `odyssey.json` — scenes and images. `src` links to the original file, `display` is Commons' 1280 px rendering, and `head` holds the marked position.
- `serve.py` — a tiny server that lets the page save head marks back into `odyssey.json`. Run `python3 serve.py 8000` and open http://localhost:8000.
