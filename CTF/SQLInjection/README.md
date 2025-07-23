# SQL Injection CTF Challenge

## Description
A simple vulnerable web app for practicing SQL Injection. Login as admin to get the flag!

## How to Run Locally (Docker)

1. Build the Docker image:

  ```bash
   sudo docker build -t sqlinj-ctf .
   ```

2. Run the container:

   ```bash
    sudo docker run -p 8080:80 sqlinj-ctf
   ```

3. Open your browser and go to [http://localhost:8080](http://localhost:8080)

## Files
- `index.html` - Main page
- `index.html` - Login form
- `login.php` - Vulnerable login logic
- `database.sql` - DB schema
- `entrypoint.sh` - DB setup on container start



<details>
  <summary>Sample solution</summary>
  admin' --
</details>
