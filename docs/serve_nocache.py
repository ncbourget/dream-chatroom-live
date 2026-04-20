from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
	def end_headers(self) -> None:
		self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
		self.send_header("Pragma", "no-cache")
		self.send_header("Expires", "0")
		super().end_headers()


if __name__ == "__main__":
	server = ThreadingHTTPServer(("0.0.0.0", 8000), NoCacheHandler)
	print("Serving no-cache HTTP on 0.0.0.0:8000")
	server.serve_forever()