# Server-Side Request Forgery (SSRF).

---

## Description

> A developer made a simple web tool to "fetch URLs" using a web form.
> Can you trick it into accessing a secret file that's meant to stay hidden?

Your objective:  
Trick the proxy to retrieve the flag hidden at `/flag.txt`
Flag format: `CTF{...}`

---

## How to Run Locally 
1. Make sure you have **Python 3** installed.

2. Open a terminal and run:

```bash
python3 app.py
