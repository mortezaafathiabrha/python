import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8000"))

PAGE = """<!DOCTYPE html>
<html>
<head>
    <title>Hello World - Python</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: linear-gradient(135deg, #3776ab 0%, #ffd43b 100%); }
        .container { text-align: center; color: white; }
        h1 { font-size: 3em; margin: 0; }
        p { font-size: 1.2em; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World!</h1>
        <p>Welcome to Python</p>
    </div>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Listening on http://0.0.0.0:{PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
