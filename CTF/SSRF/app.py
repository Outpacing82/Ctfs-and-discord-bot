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
        # Hint: match the header
        headers = {"X-Internal-SSRF": "1"}
        r = requests.get(url, timeout=2, headers=headers)
        return r.text
    except Exception as e:
        return f"Error: {e}"

@app.route("/flag")
def flag():
  if request.headers.get("X-Internal-SSRF") == "1":
    return "CTF{ssrf_is_fun}"
  return "Access Denied", 403
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)