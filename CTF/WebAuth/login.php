<?php
// Simple username-password map
$users = [
    'guest' => 'guest123',
    'user' => 'userpass',
];

// Get login info
$username = $_POST['uid'] ?? '';
$password = $_POST['pwd'] ?? '';

// Validate
if (isset($users[$username]) && $users[$username] === $password) {
    // Create base64-encoded cookie
    $data = json_encode(['user' => $username]);
    $encoded = base64_encode($data);
    setcookie("auth", $encoded, time() + 3600);
    header("Location: flag.php");
    exit;
} else {
    echo "Invalid credentials.";
}
