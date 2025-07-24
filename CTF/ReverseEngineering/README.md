# Reverse Engineering

## Description
The hardest CTF challenge amongst the list I made! Try to decode the key!

## How to Run Locally

1. Compile the C code:

  ```bash
    gcc app.c -o app
  ```

## Files
- `app.c` - Main functionality

## Note
- The flag is stored in the database for the admin user.

<details>
  <summary>Sample solution</summary>

```python
key = [0x1F, 0x3C, 0x2A, 0x55, 0x66, 0x7B, 0x12, 0x10, 0x1E, 0x33]
target = [0x46, 0x5B, 0x57, 0x3A, 0x03, 0x1F, 0x71, 0x75, 0x65, 0x52]

password = ''.join([chr(t ^ k) for t, k in zip(target, key)])
print("Recovered password:", password)
```
</details>