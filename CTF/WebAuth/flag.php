<?php
if (!isset($_COOKIE['auth'])) {
    echo "Not logged in.";
    exit;
}

$cookie = base64_decode($_COOKIE['auth']);
$data = json_decode($cookie, true);

if (!isset($data['user']) || $data['user'] !== 'admin') {
    echo "Access denied. Admins only.";
    exit;
}

$flag = trim(file_get_contents("flag.txt"));
echo "<h2>Welcome, admin!</h2>";
echo "<p>Your flag is: <code>$flag</code></p>";
?>
