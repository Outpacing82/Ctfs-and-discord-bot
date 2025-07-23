# app.py (Flask-based)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>URL Fetcher</h1>
        <form method="GET" action="/fetch">
            <input type="text" name="url" placeholder="http://example.com">
            <input type="submit">
        </form>
    '''

@app.route("/fetch")
def fetch():
    url = request.args.get("url", "").strip()
    if not url:
        return "No URL provided", 400
    try:
        # Dangerous SSRF-vulnerable fetch
        r = requests.get(url, timeout=2)
        return r.text
    except Exception as e:
        return f"Error: {e}"

@app.route("/flag")
def flag():
  if request.remote_addr == "127.0.0.1":
    return "CTF{ssrf_is_fun}"
  return "Access Denied", 403
