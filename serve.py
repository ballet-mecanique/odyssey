"""Serve index.html and let the page save head positions back into odyssey.json (HTTP PUT)."""
import http.server, json, os, sys
DIR = os.path.dirname(os.path.abspath(__file__))
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=DIR, **k)
    def do_PUT(self):
        if self.path.split('?')[0] != '/odyssey.json': return self.send_error(403)
        body = self.rfile.read(int(self.headers['Content-Length']))
        json.loads(body)  # refuse anything that isn't valid JSON
        tmp = os.path.join(DIR, 'odyssey.json.tmp')
        open(tmp, 'wb').write(body); os.replace(tmp, os.path.join(DIR, 'odyssey.json'))
        self.send_response(204); self.end_headers()
http.server.ThreadingHTTPServer(('', int(sys.argv[1]) if len(sys.argv) > 1 else 8000), H).serve_forever()
