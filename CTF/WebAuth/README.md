# Web - Authentication

---

## Description

> Only the admin has access to the secret flag through a portal.
> Can you log in as the admin and retrieve the flag?

Your objective:  
Trick the proxy to retrieve the flag hidden at `/flag.txt`
Flag format: `CTF{...}`

---

## How to Run Locally 

1. Install php if you haven't already.

  ```bash
    sudo apt install php8.1-cli
  ```
2. Open a terminal and run:

```bash
php -S localhost:8080
```

## Files
- `app.py` - Main page and functionality

<details>
  <summary>Sample solution</summary>
  Enter "admin" into the user field, then access the protal directly.
</details>
