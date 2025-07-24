# Cross-Site Scripting(XSS) CTF Challenge

## Description
A simple vulnerable web app for practicing XSS. Pop an alert to get the flag!

## How to Run Locally (PHP)

1. Install php if you haven't already.

  ```bash
    sudo apt install php8.1-cli
  ```

2. Start up the server.

  ```bash
    php -S localhost:8080
  ```

3. Open your browser and go to [http://localhost:8080](http://localhost:8080)

## Files
- `index.php` - Main page and functionality

<details>
  <summary>Sample solution</summary>
  Copy this into the browser
  ```bash
    http://localhost:8080/index.php?name=%3Cscript%3Ealert(1)%3C/script%3E
  ```
</details>
