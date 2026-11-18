import sys, os, threading, webbrowser, shutil, subprocess
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 8765
BASE = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
URL = f"http://127.0.0.1:{PORT}/inventario.html"

class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=BASE, **k)
    def log_message(self, *a): pass

def abrir():
    for exe in ("chrome", "msedge"):
        p = shutil.which(exe)
        if not p:
            for root in (os.environ.get("ProgramFiles"), os.environ.get("ProgramFiles(x86)"), os.environ.get("LOCALAPPDATA")):
                for sub in (r"Google\Chrome\Application\chrome.exe", r"Microsoft\Edge\Application\msedge.exe"):
                    c = os.path.join(root or "", sub)
                    if os.path.exists(c): p = c; break
                if p: break
        if p:
            subprocess.Popen([p, f"--app={URL}"]); return
    webbrowser.open(URL)

if __name__ == "__main__":
    try:
        srv = ThreadingHTTPServer(("127.0.0.1", PORT), H)
    except OSError:
        abrir(); sys.exit()          # ya estaba abierto
    threading.Timer(0.6, abrir).start()
    srv.serve_forever()
